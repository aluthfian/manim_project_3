from PIL import Image
import requests


class setOpacity(Scene):
    def construct(self):
        opac_num = DecimalNumber().to_edge(UP)
        Rect = Rectangle(width=4, height=3, color=BLUE_B, fill_opacity=1)
        Rect = Rect.set_stroke(BLUE_B, opacity=1.0)
        
        self.add(Rect, opac_num)
        
        vt = ValueTracker(10)
        
        opac_num.add_updater(lambda d: d.set_value(vt.get_value()/10))
        Rect.add_updater(lambda d: d.set_opacity(vt.get_value()/10))
        
        self.play(vt.animate.set_value(3), run_time=5, rate_func=linear)
        self.wait()


class ValueTrackerTest(Scene):
    def construct(self):
        img = Image.open(requests.get(r'https://pbs.twimg.com/media/E-Bghn9VIAQZ_ng?format=jpg&name=small', stream=True).raw)
        img = ImageMobject(img)
        img.scale(1.0)

        num = DecimalNumber(0)
        num.next_to(img, DOWN)
        t = Text("Opacity:", stroke_width=0, size=0.4).next_to(num, LEFT)

        self.add(img, t, num)
        self.wait()

        vt = ValueTracker(10)

        num.add_updater(lambda m:m.set_value(vt.get_value()/10))
        img.add_updater(lambda m: m.set_opacity(vt.get_value()/10))

        self.play(vt.animate.set_value(5), run_time=5, rate_func=linear)
        self.wait()
  

class TextTest(Scene):
    def construct(self):
        a = Tex(r"$$ P_n{ =}{ {{ {\lambda }^n} }\over {n {!} } } e^{ { -}\lambda } $$ ") 
        
        self.add(a)
        b = a.copy()
        b[0][6:8].set_color(BLUE_D) #select only indices 6 to 7 from b
        c = b.copy()
        c[0][3:5].set_color(PURE_RED) #select only indices 2 to 3 from c
        self.wait()
        self.play(Transform(a,b)) #transforms a to b
        self.wait()
        self.play(Transform(b,c)) #transforms b to c
        self.wait()
