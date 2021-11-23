d = 60
x = 0
y = 0
import arcade
arcade.open_window(400, 400, "Will Fuchs")
arcade.set_background_color(arcade.color.WHITE)
arcade.start_render()
#Background
for i in range(20):
    arcade.draw_line(x, y, x, 400, arcade.color.BLACK)
    x += 20
for i in range(20):
    arcade.draw_line(0, y, 400, y, arcade.color.BLACK)
    y += 20
#Disc Case
arcade.draw_rectangle_filled(200, 200, 300, 300, arcade.color.LIGHT_GRAY)
arcade.draw_rectangle_outline(200, 200, 300, 300, arcade.color.BLACK, 6)
#Disc
arcade.draw_circle_filled(200, 200, 140, arcade.color.HELIOTROPE_GRAY)
arcade.draw_circle_outline(200, 200, 140, arcade.color.BLACK, 6)
arcade.draw_circle_filled(200, 200, 60, arcade.color.WHITE)
arcade.draw_circle_filled(200, 200, 25, arcade.color.GRAY)
arcade.draw_circle_filled(200, 200, 10, arcade.color.WHITE)
arcade.draw_circle_outline(200, 200, 10, arcade.color.BLACK, 3)
for i in range(2):
    arcade.draw_circle_outline(200, 200, d, arcade.color.BLACK, 4)
    d -= 25
#Pink Thing
arcade.draw_rectangle_filled(300, 200, 110, 85, arcade.color.FUCHSIA_PINK)
arcade.draw_rectangle_outline(300, 200, 110, 85, arcade.color.BLACK, 2)
#Text
arcade.draw_text("80", 260, 245, arcade.color.BLACK, 30)
arcade.draw_rectangle_outline(210, 110, 40, 40, arcade.color.BLACK)
arcade.draw_text("M", 192, 107, arcade.color.BLACK, 15)
arcade.draw_text("D", 192, 92, arcade.color.BLACK, 15)
arcade.draw_rectangle_filled(200, 25, 150, 45, arcade.color.LIGHT_FUCHSIA_PINK)
arcade.draw_rectangle_outline(200, 25, 150, 45, arcade.color.BLACK, 3)
arcade.draw_text("YANDHI", 126, 5.5, arcade.color.PALATINATE_PURPLE, 30, 200, "left",)
arcade.draw_text("YANDHI", 129, 7, arcade.color.BLACK, 30, 200, "left")
arcade.finish_render()
arcade.run()
