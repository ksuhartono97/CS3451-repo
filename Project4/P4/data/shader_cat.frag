#define PROCESSING_TEXTURE_SHADER

#ifdef GL_ES
precision mediump float;
precision mediump int;
#endif

uniform sampler2D texture;

varying vec4 vertColor;
varying vec4 vertTexCoord;

void main() {
  vec4 diffuse_color = vec4(0,0,0,0);
  for(int i = -10; i < 11; i++) {
    float offset = i / 256.0;
    vec2 offsetxy = vec2(vertTexCoord.x + offset, vertTexCoord.y);
    diffuse_color += texture2D(texture, offsetxy);
  }
  diffuse_color = diffuse_color/21.0;
  gl_FragColor = vec4(diffuse_color.rgb, 1.0);
}
