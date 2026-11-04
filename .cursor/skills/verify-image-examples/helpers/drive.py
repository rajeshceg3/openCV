#!/usr/bin/env python3
"""Drive actual desktop image scripts on an owned isolated virtual display."""
import argparse,datetime,json,os,pathlib,shutil,subprocess,time,select
root=pathlib.Path(__file__).resolve().parents[4]
p=argparse.ArgumentParser();p.add_argument('mode',choices=['doctor','drive']);p.add_argument('--out',default='.verification-evidence');a=p.parse_args();out=pathlib.Path(a.out).resolve();out.mkdir(parents=True,exist_ok=True)
r={'mode':a.mode,'at':datetime.datetime.now(datetime.timezone.utc).isoformat(),'ok':False,'steps':[]};display=None;child=None
try:
 import cv2
 for tool in ['Xvfb','xdotool','import']:assert shutil.which(tool),tool+' required'
 for f in ['faces.png','coins.png','noisy.png']:assert cv2.imread(str(root/f)) is not None,f+' unreadable'
 r['opencv']=cv2.__version__
 if a.mode=='drive':
  # Xvfb chooses an unused display and reports it via a private pipe.
  read,write=os.pipe();display=subprocess.Popen(['Xvfb','-displayfd',str(write),'-screen','0','1600x1000x24','-nolisten','tcp'],pass_fds=[write],stdout=subprocess.DEVNULL,stderr=subprocess.PIPE);os.close(write)
  assert select.select([read],[],[],8)[0],'Display startup timeout'
  with os.fdopen(read) as pipe:number=pipe.readline().strip()
  assert number.isdigit(),'Virtual display failed';env={**os.environ,'DISPLAY':':'+number}
  scripts=[('smoothImage.py','Smoothed image'),('crop.py','After Crop'),('grayscale.py','Gray'),('resizeImage.py','Resized Image'),('edgeDetection.py','After Edge Detection'),('rotateImage.py','Rotated Image'),('shapes.py','Rectangular Image'),('dimensions_color.py','Hall of faces')]
  for script,title in scripts:
   child=subprocess.Popen([os.sys.executable,str(root/script)],cwd=root,env=env,stdout=subprocess.PIPE,stderr=subprocess.PIPE,text=True)
   wid=None
   for _ in range(60):
    q=subprocess.run(['xdotool','search','--onlyvisible','--name','^'+title+'$'],env=env,capture_output=True,text=True)
    if q.returncode==0:wid=q.stdout.strip().splitlines()[0];break
    if child.poll() is not None:break
    time.sleep(.1)
   assert wid,(script,'No expected desktop window',child.stderr.read() if child.poll() is not None else '')
   # Allow the real paint to finish, capture the actual desktop window, then a key exits waitKey.
   time.sleep(.25);capture=out/(script+'.png');subprocess.run(['import','-window',wid,str(capture)],env=env,check=True,timeout=8)
   subprocess.run(['xdotool','key','--window',wid,'space'],env=env,check=True,timeout=5)
   stdout,stderr=child.communicate(timeout=8);assert child.returncode==0,(script,stderr)
   r['steps'].append({'script':script,'window_title':title,'exit':child.returncode,'stdout':stdout,'stderr':stderr,'screenshot':str(capture)});child=None
  # Actual input/output math contract for the corrected smoothing parameters, separate from GUI proof.
  import numpy as np
  image=cv2.imread(str(root/'noisy.png'));blur=cv2.GaussianBlur(image,(13,13),1);assert blur.shape==image.shape and not np.array_equal(blur,image)
  cv2.imwrite(str(out/'smooth-output.png'),blur);r['steps'].append({'smoothing_shape':list(blur.shape),'changed_pixels':int(np.count_nonzero(blur!=image))})
 r['ok']=True
except Exception as e:r['failure']=str(e)
finally:
 if child and child.poll() is None:child.terminate();child.wait(timeout=5)
 if display and display.poll() is None:display.terminate();display.wait(timeout=5)
(out/(a.mode+'.json')).write_text(json.dumps(r,indent=2)+'\n');print(json.dumps(r,indent=2));raise SystemExit(0 if r['ok'] else 1)
