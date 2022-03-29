from kivymd.app import MDApp
from kivy.lang.builder import Builder

kv = '''
<MySwiper@MDSwiperItem>:
    Image:
        source: "0_start.jpg"
        radius: [20,]


Screen:
    BoxLayout:
        orientation: 'vertical'
    
        MDSwiper:
            
    

            MySwiper:
            
            MySwiper:
        
        MDSwiper:
            
    

            MySwiper:
            
            MySwiper:
            
        
                       
                       
        
        
'''


class Main(MDApp):
    def build(self):
        return Builder.load_string(kv)

Main().run()