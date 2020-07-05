from pkg.usuario_facade import UsuarioFacade

def main():
    facade = UsuarioFacade()
    
    #result = facade.get_user_by_id(1)
    #print(result)

    #result = facade.get_all_user_by_id('1,2,4,6')
    #print(result)
    #print(len(result))
    #print(result.rowcount)
    #print(result.rows)
    #for row in result.rows:
    #    print(row[1])

    #result = facade.get_user_by_matricula('c110611')
    #print(result.rows)
    #print(result.rowcount)
    #facade.get_all_users_by_nome('ilso')

    facade.create_user('C110611', 'MAURO', '1234', 'ADM')
    facade.create_user('C110612', 'LUC', '1234', 'NORMAL')

    #result = facade.get_all_user_by_matricula('c11')
    #print(result.rowcount)
    #print(result.rows)
    #t = facade.to_all_usuario()
    #print(len(t))
    #for obj in t:
    #    print (obj.matricula)

    #usuario = facade.update_user(1, 'C110611', 'mauro yukio', '1234')
    #print(usuario.id)
    #print(usuario.matricula)
    #print(usuario.nome)
    #print(usuario.senha)

    #usuario = facade.delete_user_by_id(3)
    #print(usuario)

    #result = facade.delete_user_by_ids('2,4')
    #print(result.rowcount)
    #print(result.rows)

if __name__ == "__main__":
    main()