import __main__ as main
import os,math
def Init():
    global objects
    moudles={}
    objects={}
    player=main.player
    for file in os.listdir("objects"):
        if file.endswith('.py')and file != '__init__.py':
            name = file[:-3]
            moudle=__import__(name,fromlist=['*'])
            moudle.ImgUpdate=ImgUpdate
            moudles[name]=moudle
    for moudle in moudles.values():
        name=moudle.__name__
        image=moudle.originimage
        variable=moudle.variable
        istrigger=moudle.istrigger
        supplement=moudle.supplement
        index=moudle.index
        if variable:variable+=","
        def OnCollision(self,collider):
            if "Collision"in self.trigger and self.trigger["Collision"][0]!="pass":
                self.running.append(list(self.trigger["Collision"]))
                self.collider=collider
                if self.trigger["Collision"][-1]!="save":
                    self.trigger["Collision"].insert(0,"pass")
            self.moudle.OnCollision(self,collider)
        mark="{}"
        code=f'''
global obj
group=main.pygame.sprite.Group()
group.index={index}
main.groups["{name}"]=group
class {name}(main.pygame.sprite.Sprite):
    def __init__(self,xy,{variable}trigger={mark},rotation=0,size=(1,1),flip=(0,0),image=main.pygame.image.load({image}).convert_alpha(),name=False):
        super().__init__()
        self.xy,self.trigger=list(xy),trigger
        self.offset,self.anchor,self.running=[0,0],[0,0],[]
        self.istrigger,self.loop={istrigger},[]
        self.type="{name}"
        self.group=main.groups["{name}"]
        main.groups["{name}"].add(self)
        if not name:self.name="{name}-"+str(len(main.groups["{name}"]))
        else:self.name=name
        self.ImgUpdate=ImgUpdate
        {supplement}
        self.collider,self.origin=None,None
        self.ImgUpdate(self,rotation,size,flip,image)
    def Clear(self):
        main.groups["{name}"].empty()
        return True
    def Delete(self):
        main.groups["{name}"].remove(self)
        return True
obj={name}'''
        exec(code)
        obj.Run=Run
        obj.update=ObjectUpdate
        obj.OnCollision=OnCollision
        obj.moudle=moudle
        objects[name.capitalize()]=obj
def Update():
    for index in range(10):
        for groups in main.groups.values():
            if groups.index==index:groups.update()
def Delete():
    for groups in main.groups:
        main.groups[groups].empty()
def ImgUpdate(self,rotation=0,size=False,flip=False,image=False):
    if image:
        if type(image)==str or type(image)==bytes:self.image=main.pygame.image.load(image).convert_alpha()
        else:self.image=image
        self.rect=self.image.get_rect()
    if size:self.image=main.pygame.transform.smoothscale(self.image,(size[0]*40,size[1]*40))
    if flip:self.image=main.pygame.transform.flip(self.image,*flip)
    if rotation:
        data=self.image.get_size()
        self.image = main.pygame.transform.rotate(self.image,rotation)
        rotation=math.radians(rotation)
        d=(self.anchor[0]**2+self.anchor[1]**2)**0.5
        self.offset=[d*math.cos(rotation)-self.anchor[0]+(data[0]-self.image.get_size()[0])/2,
                           -d*math.sin(rotation)-self.anchor[1]+(data[1]-self.image.get_size()[1])/2];
    self.rect=self.image.get_rect()
    self.rect.center=[self.xy[0]*40,self.xy[1]*40]
def Run(self,index=0):
    funcs=self.running[index]
    match funcs[0]:
        case"exit":del self.running[index]
        case"loop":pass
        case"save":
            self.running[index].append(self.running[index].pop(0))
            self.trigger[self.running[index].pop(0)].pop(0)
            del self.running[index]
        case _:
            if funcs[0](self):
                if "loop" in self.running[index] or "save" in self.running[index]:
                    self.running[index].append(self.running[index][0])
                self.running[index].pop(0)
                if not self.running[index]:
                    del self.running[index]
    if index+1<len(self.running):
        Run(self,index+1)#只运行每列第一项
def ObjectUpdate(self):
    self.moudle.Update(self)
    for i in self.trigger:
        if i!="Collision" and i(self) and self.trigger[i][0]!="pass":#判断是否执行
            if self.trigger[i][-1]=="save":
                self.trigger[i].append(i)
            self.running.append(list(self.trigger[i]))#执行
            self.trigger[i].insert(0,"pass")
    if self.running:
        self.Run()
    self.rect.center =[(self.xy[i]+main.Game.xy[i])*40 for i in (0,1)]
    if self.rect.bottom>=0 and self.rect.top<=main.screen.get_size()[1] and self.rect.right>=0 and self.rect.left<=main.screen.get_size()[0]:
        main.screen.blit(self.image,[self.offset[i]+self.rect.topleft[i]for i in [0,1]])
