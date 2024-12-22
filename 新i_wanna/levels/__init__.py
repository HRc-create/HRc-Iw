import __main__ as main
UI=main.UI
def Init():
    UI.Text("title",main.screen.get_rect().center,"i wanna go for sleep",wordsize=100,size=(0,-main.screen.get_size()[1]/2),page="title")
    UI.Button("StartButton",(main.screen.get_size()[0]/2-200,main.screen.get_size()[1]/3*2),(400,200),func=main.Game.Load,page="title")
    UI.Text("StartButtonText",(main.screen.get_size()[0]/2,main.screen.get_size()[1]/3*2),"Start",wordsize=100,size=(0,200),page="title")
    UI.Text("GameOver0",main.screen.get_rect().center,"Game Over","#fabcde",wordsize=200,size=(0,-main.screen.get_size()[1]/2),page=2)
    UI.Text("GameOver1",(main.screen.get_size()[0]/2,main.screen.get_size()[1]/3*2),"按 \"R\" 起 床",wordsize=100,size=(0,main.screen.get_size()[1]/8),page=2)
    UI.Text("WinText",main.screen.get_rect().center,"Won!!!!!!","#ffff00",wordsize=200,size=(0,-main.screen.get_size()[1]/2),page=3)
    UI.Text("Author",(main.screen.get_size()[0]/2,main.screen.get_size()[1]/3*2),"Made by Frog-HRC",wordsize=100,size=(0,-main.screen.get_size()[1]/2),page=3)
    if main.Game.savexy[0]=="initing":
        main.Game.savexy=[2,15]
    main.player.xy=list(main.Game.savexy)
