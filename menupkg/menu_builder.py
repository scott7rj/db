from menupkg.menu1_facade import Menu1Facade
from menupkg.menu2_facade import Menu2Facade

class MenuBuilder(object):
    def __init__(self):
        self.menu = ''
        
    def __repr__(self):
        return f"Menu('{self.menu}')"

    def build(self, perfil):
        menu1_facade = Menu1Facade()
        menu2_facade = Menu2Facade()

        menu1_facade.get_all_active_menu1_by_perfil(perfil)
        t = menu1_facade.to_all_menu1()
        for obj in t:
            print (obj.nome)
        #for row in result.rows:
        #    print(row.nome)
        menu_begin = "<nav><ul class='menu'>"
        menu_items = ''
        for obj in t:
            menu_items += f"<li><a href='#'>{obj.nome}</a>"
            
            menu2_facade.get_all_active_menu2_by_menu1(obj.id)
            t2 = menu2_facade.to_all_menu2()
            menu_items += "<ul>"
            for obj in t2:
                if obj.target:
                    menu_items += f'<li><a href="#" onclick="{obj.target}">{obj.nome}</a>'
                else:
                    #TODO montar o 3 nivel
                    menu_items += f'<li><a href="#">{obj.nome}</a>'
                    

            menu_items += "</ul>"    

            menu_items += f"</li>"

        menu_end = "</ul></nav>"

        return menu_begin + menu_items + menu_end

"""
<ul>
    <li><a href="#">TDS</a>
        <ul>
            <li><a href="#" onclick="target999('<?php echo $profile; ?>','DB2-TDS-STATS');">ESTATÍSTICAS</a></li>
        </ul>
    </li>
</ul>
"""