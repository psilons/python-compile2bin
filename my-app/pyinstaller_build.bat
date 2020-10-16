rmdir /Q /S build
rmdir /Q /S dist

pyinstaller --clean --onefile --noupx --name klotski_app  --icon app.ico^
    --paths=src\my_app --hidden-import my_lib.stack_queue_impl^
    --exclude-module tkinter^
    src\my_app\klotski_app.py
