# Layout 
***

Say, you're wanted to build a home with different room and function inside so you need to set it size, doors and
the other stuff. layout is also do like room in your application after you create one placed them into directory
`model/layout` and then you define it into `Alias`

**Attention**:

     when you create your layout make sure you create your package first, for example "model/layout/welcome/" It also necessary for widget and controller.

There's some type of layout which is: *Anchor, Box, Float, Grid, Modal* **(Experimental not stable)** *, Popup*

| Layout | Description |
| -- | -- |
| [Anchor](https://kivy.org/docs/api-kivy.uix.anchorlayout.html) | layout is used to aligned everything what inside it. |
| [Box](https://kivy.org/docs/api-kivy.uix.boxlayout.html) | Box is arranged layout, everything inside Box Layout will be arranged based on it's orientation. |
| [Float](https://kivy.org/docs/api-kivy.uix.floatlayout.html) | Float is only order the position and size hint children. |
| [Grid](https://kivy.org/docs/api-kivy.uix.gridlayout.html) | Grid is take the children into matrix position, it takes the available space and divide into coloumns and row. |
| [Modal](https://kivy.org/docs/api-kivy.uix.modalview.html) | Modal is an modal view layout when it open it will cover the parent with overlay layout.|
| [Popup](https://kivy.org/docs/api-kivy.uix.popup.html) | Same as modal but it's a popup with title and only one content inside. |

***Warning !*** *Modal layout is still experimental and currently not stable.*

## Behavior method
- **gathering**, gathering is used to collecting some layout or widget into the layout it self. there's two ways how to gathering *listing* and *directing*, if you use *listing* gathering object will be reverted when the layout is called again if you use *directing* way layout will gather more object no matter how much it called.

- **adding**, adding is used to adding the collected item from layout it self, and add the as children.

- **removing**, removing adalah kebalikan dari adding.