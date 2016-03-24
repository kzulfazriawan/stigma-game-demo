# Widget
***

## What is widget
if you had to know layout before now we would tell you about widget. Widget is like your home interior, *television*,
*sofa*, *lamp* and many more. widget is like interior in your application, the widget is placed inside directory
`model/widget` and then you need to define it into `Alias`

**Attention**:

     when you create your layout make sure you create your package first, for example "model/widget/welcome/" It also necessary for layout and controller.
     
There's some type of widget which is *Button, Image, Input, Label, and Radio*. each widget had different functionality.

| 0:0 | 1:0 |
| -- | -- |
| [Button](https://kivy.org/docs/api-kivy.uix.button.html) | Button is triggered text with press event. |
| [Image](https://kivy.org/docs/api-kivy.uix.image.html) | Image is an widget containing texture image. |
| [Input](https://kivy.org/docs/api-kivy.uix.textinput.html) | Input, input is aliased from Textinput. |
| [Radio](https://kivy.org/docs/api-kivy.uix.togglebutton.html) | Radio is aliased from ToggleButton, it can grouped into many button. |

## Behavior method
- **bound**, bound is used to attach some object into widget based on it's event.
- **placeholder**, used for set temporary text in input the text will disappear if input is focused by cursor.