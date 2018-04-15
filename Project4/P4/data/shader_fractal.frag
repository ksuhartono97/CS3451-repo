#define PROCESSING_COLOR_SHADER

#ifdef GL_ES
precision mediump float;
precision mediump int;
#endif

varying vec4 vertColor;
varying vec4 vertTexCoord;

void main() {
  float tmpval;
  int iter;
  float tempreal, tempimag, Creal, Cimag, tempreal2, tempimag2;
  float r2;
  Creal = (vertTexCoord.s * 6.0) - 2.0;
  Cimag = (vertTexCoord.t * 6.0) - 3.0;
  float real = 0.5;
  float imag = 0;

  for (iter = 1; iter < 20; iter++) {
    tempreal = real;
    tempimag = imag;
    float re = (1.0-tempreal);
    float im = -tempimag;
    tempreal2 = Creal * tempreal - Cimag * tempimag;
    tempimag2 = Creal * tempimag + Cimag * tempreal;
    real = tempreal2 * re - tempimag2 * im;
    imag = tempreal2 * im + tempimag2 * re;
    r2 = (real * real) + (imag * imag);
    if (r2 >= 4)
      break;
    }
    vec4 color;
    if (r2 >= 4)
    color = vec4(1.0, 0.0, 0.0, 1.0);
    else
    {
    color = vec4 (1.0, 1.0, 1.0, 1.0);
    }
    gl_FragColor = color;
  //gl_FragColor = vec4(1.0, vertTexCoord.t, vertTexCoord.t, 1.0);
}
