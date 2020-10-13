---
title: VSCode之Shader插件
date: 2020-10-12 22:45:18
tags:
---
# Shader插件 VSCode
## 0、推荐原因
可以i很快的验证一些渲染问题。
<!-- more -->

## 1、ShaderToy网址
https://www.shadertoy.com/view/4dXGR4

![file](http://jeff.spring4all.com/FgYh43AWI02JWNJ-6SncSzGqwQ7T)
![file](http://jeff.spring4all.com/Fu-8G0vm381z1rX3KKfTicF3uxKj)

## 2、VSCode插件
### 2.1、安装
![file](http://jeff.spring4all.com/Fo_raOcAmtq67vB1yfVNn3r67Yrk)


### 2.1、Hello world
1. 新建一个文件 test.shader
2. 里面写如下代码：
```
void main() {
  float time = iGlobalTime * 1.0;
  vec2 uv = (gl_FragCoord.xy / iResolution.xx - 0.5) * 8.0;
  vec2 uv0 = uv;
  float i0 = 1.0;
  float i1 = 1.0;
  float i2 = 1.0;
  float i4 = 0.0;
  for (int s = 0; s < 7; s++) {
    vec2 r;
    r = vec2(cos(uv.y * i0 - i4 + time / i1), sin(uv.x * i0 - i4 + time / i1)) / i2;
    r += vec2(-r.y, r.x) * 0.3;
    uv.xy += r;
 
    i0 *= 1.93;
    i1 *= 1.15;
    i2 *= 1.7;
    i4 += 0.05 + 0.1 * time * i1;
  }
  float r = sin(uv.x - time) * 0.5 + 0.5;
  float b = sin(uv.y + time) * 0.5 + 0.5;
  float g = sin((uv.x + uv.y + sin(time * 0.5)) * 0.5) * 0.5 + 0.5;
  gl_FragColor = vec4(r, g, b, 1.0);
}
```

3、右键预览
![file](http://jeff.spring4all.com/Fg7ruQZf7AAH5BzZaHsOhmvgImWH)

![file](http://jeff.spring4all.com/FoV0q3WutAoDXhWmQSF7K-B9v71Z)
