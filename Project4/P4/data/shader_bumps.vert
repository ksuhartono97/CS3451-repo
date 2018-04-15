#define PROCESSING_TEXTURE_SHADER

uniform mat4 transform;
uniform mat4 texMatrix;

attribute vec4 position;
attribute vec4 color;
attribute vec3 normal;
attribute vec2 texCoord;

varying vec4 vertColor;
varying vec4 vertTexCoord;

uniform sampler2D texture;

void main() {
  vertColor = color;
  vertTexCoord = texMatrix * vec4(texCoord, 1.0, 1.0);

  vec4 textureColor = texture2D(texture, vertTexCoord.st);
  float intensity = 1 - ((textureColor.r * 0.3) + (textureColor.g * 0.6) + (textureColor.b * 0.1));

  vec4 pos = position;
  vec3 xyz_Altered = pos.xyz + (normal * intensity * 20);
  vec4 altered_Pos = vec4(xyz_Altered, pos.w);
  gl_Position = transform * altered_Pos;
}
