#define PROCESSING_COLOR_SHADER

#ifdef GL_ES
precision mediump float;
precision mediump int;
#endif

varying vec4 vertColor;
varying vec4 vertTexCoord;

void main() {
  float radius = 0.05;
  float alpha = 0;
  vec2 center = vec2(0.5, 0.5);
  vec2 pos = vec2(vertTexCoord.s, vertTexCoord.t);
  pos -= center;
  float dist = sqrt(dot(pos, pos));

  for(int i = 20; i >= 1; i--) {
    if (i%2==0) {
      alpha = 0;
    }
    else {
      alpha = 0.7;
    }
    float circle_radius = radius * i;
    if(dist < circle_radius) {
      gl_FragColor =  vec4(0.2, 0.4, 1.0, alpha);
    }
  }
}
