from controller.Functions import *
from model.databaseModel import setup_db
from view.views import MainMapWindow

setup_db()
setup_api_keys()

#get_map_image(-28.9486767,-49.4689805,-28.9513217,-49.4638693)

#tela_default.start_window_loop()

debug_print("HELLO WORLD!")
app = MainMapWindow()
app.mainloop()


# get_map_image(-28.9486767,-49.4689805,-28.9513217,-49.4638693)
