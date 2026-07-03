from controller.Functions import setup_api_keys
from model.databaseModel import setup_db
from view.views import MainMapWindow,DetailView
from controller.C_shared import debug_print


setup_db()
setup_api_keys()

#get_map_image(-28.9486767,-49.4689805,-28.9513217,-49.4638693)

#tela_default.start_window_loop()


debug_print("Program is in debug mode, to disable it set DEBUG = false in src/controller/C_shared.py")
debug_print("HELLO WORLD!")
debug_print("Testing Detail view")




app = MainMapWindow()
app.mainloop()


# get_map_image(-28.9486767,-49.4689805,-28.9513217,-49.4638693)
