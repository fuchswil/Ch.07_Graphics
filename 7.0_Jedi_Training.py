#Sign your name:Will Fuchs

'''
Recreate, exactly the Test Picture from the website. The arcade colors used in this picture in no particular order are:
BLACK, ALMOND, PHLOX, BLUSH, RED, BLUE, WISTERIA, AMBER, BRICK_RED and YELLOW.
The picture is 500px wide and 400px tall. Look up ARC in the documentation to do the PAC-MAN.
'''
import arcade
SW = 500
SH = 400
arcade.open_window(SW, SH, "Ch. 7 Jedi Training")
arcade.set_background_color(arcade.color.ALMOND)
arcade.start_render()
#vertical lines
for x in range(0, SW, 20):
    arcade.draw_rectangle_filled(x, 300, 1, 600, arcade.color.BLACK)
#horizontal lines
for y in range(0, SH, 20):
    arcade.draw_rectangle_filled(250, y, 600, 1, arcade.color.BLACK)
arcade.draw_circle_filled(250, 200, 40, arcade.color.WISTERIA)
arcade.draw_rectangle_filled(50, 370, 58, 18, arcade.color.PHLOX)
arcade.draw_line(80, 20, 120, 60, arcade.color.BLUE)
arcade.draw_ellipse_filled(100, 100, 120, 40, arcade.color.AMBER)
arcade.draw_text("I love you, I know.", 22, 155, arcade.color.RED, 20)
arcade.draw_arc_filled(400, 320, 120, 120, arcade.color.YELLOW, 30, 330)
arcade.draw_rectangle_filled(200, 260, 40, 20, arcade.color.BRICK_RED, 315)
arcade.draw_point(460, 10, arcade.color.RED, 5)
arcade.finish_render()
arcade.run()