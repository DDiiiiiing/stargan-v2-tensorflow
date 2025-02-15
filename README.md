# Korean YetHangul(medival korean) Font Generator Using StarGAN v2
## used code below
### StarGAN v2 &mdash; Official TensorFlow Implementation [[Paper]](https://arxiv.org/abs/1912.01865) [[Pytorch]](https://github.com/clovaai/stargan-v2)
### Implemented by [Junho Kim](http://bit.ly/jhkim_ai)

<div align="center">
  <img src="./assets/yethangul_teaser.png">
</div>

## CAUTION
* This project is working on very specific case only.
* Font generating was only tested on 64*64 RGB image
* Some korean font are needed to run properly
* Before training, you must generate dataset 

## Requirements
* `Tensorflow == 2.1.0`
* `Tensorflow-addons == 0.9.1`
* `opencv-python`
* `Pillow`
* `tqdm`
* `gpuutil`
* `humanize`
* `fonttools`
* 네이버 나눔명조옛한글 (https://hangeul.naver.com/2014/archaicword)
* 네이버 나눔바른고딕옛한글 (https://hangeul.naver.com/2014/archaicword) optional
* 배달의민족 을지로체 (https://www.woowahan.com/) optional
* 네이버 나눔고딕 (https://hangeul.naver.com/font) optional
* 네이버 나눔고딕 (https://hangeul.naver.com/font) optional

## Usage
```
├── dataset
   └── YOUR_DATASET_NAME
       ├── train
           ├── domain1 (domain folder)
               ├── xxx.jpg (domain1 image)
               ├── yyy.png
               ├── ...
           ├── domain2
               ├── aaa.jpg (domain2 image)
               ├── bbb.png
               ├── ...
           ├── ...
           
       ├── test
           ├── ref_imgs (domain folder)
               ├── domain1 (domain folder)
                   ├── ttt.jpg (domain1 image)
                   ├── aaa.png
                   ├── ...
               ├── domain2
                   ├── kkk.jpg (domain2 image)
                   ├── iii.png
                   ├── ...
               ├── ...
               
           ├── src_imgs
               ├── src1.jpg 
               ├── src2.png
               ├── ...

        ├── practice
           ├── ref_imgs (domain folder)
               ├── domain1 (domain folder <<-- target font style)
                   ├── ttt.jpg (domain1 image <<-- 1 image. more than 1 is meaningless)

           ├── src_imgs (<<-- will be automatically generated)
               ├── text.txt (characters you want to generate)
```

### Train
```
python main.py --dataset yet_hangul --phase train --img_size 64
```

### Test
```
python main.py --dataset yet_hangul --phase test --img_size 64
```
### Practice
When you write yet hangul, each character must be one unicode. If not, program might read as 2 or more characters, rather than 1 character. Be careful if you copy from internet. Many yet hangul words written on internet are combinational. (ᄎᆞᆷ〮 <-- .+ㅊ+ . +ㅁ) Use this webpage would be helpful (https://www.korean.go.kr/common/oldHangeul.do)
```
python main.py --dataset yet_hangul --phase practice --img_size 64
```
### GenerateDataset.ipynb
```
click RUN ALL button...
```

## Tensorflow results (20K)
### Latent-guided synthesis
#### yet_hangul
<div align="center">
  <img src="./assets/yethangul_lat_result.jpg">
</div>

### Reference-guided synthesis
#### yet_hangul
<div align="center">
  <img src="./assets/yethangul_ref_result.jpg">
</div>

## Pretrained checkpoint
https://drive.google.com/file/d/1dXIQG5baItHa6-5W9ZNZnJi_1OK8lol8/view?usp=sharing

## License
The source code, pre-trained models, and dataset are available under [Creative Commons BY-NC 4.0](https://github.com/clovaai/stargan-v2/blob/master/LICENSE) license by NAVER Corporation. You can **use, copy, tranform and build upon** the material for **non-commercial purposes** as long as you give **appropriate credit** by citing our paper, and indicate if changes were made. 

For business inquiries, please contact clova-jobs@navercorp.com.<br/>	
For technical and other inquires, please contact yunjey.choi@navercorp.com.<br/>	
For questions about the tensorflow implementation, please contact jhkim.ai@navercorp.com.


## Citation
If you find this work useful for your research, please cite our paper:

```
@inproceedings{choi2020starganv2,
  title={StarGAN v2: Diverse Image Synthesis for Multiple Domains},
  author={Yunjey Choi and Youngjung Uh and Jaejun Yoo and Jung-Woo Ha},
  booktitle={Proceedings of the IEEE Conference on Computer Vision and Pattern Recognition},
  year={2020}
}
```
