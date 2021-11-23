import arcade
y = 10
sver1 = 120
sver2 = 120
arcade.open_window(494, 260, "The Stars and Stripes")
arcade.set_background_color(arcade.color.WHITE)
arcade.start_render()
for i in range(7):
    arcade.draw_rectangle_filled(245, y, 500, 20, (191, 10, 48))
    y += 40
arcade.draw_rectangle_filled(98.8, 190, 197.6, 140.04, (0, 40, 104))
for i in range(5):
    arcade.draw_text("*   *   *   *   *   *", 14, sver1, arcade.color.WHITE, 20)
    sver1 += 26
for i in range(4):
    arcade.draw_text("*   *   *   *   *", 32, sver2+14, arcade.color.WHITE, 20)
    sver2 += 26
arcade.finish_render()
arcade.run()