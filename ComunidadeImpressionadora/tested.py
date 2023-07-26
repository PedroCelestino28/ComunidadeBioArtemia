from main2 import app
from ComunidadeImpressionadora import database
from ComunidadeImpressionadora.models import Usuario
from ComunidadeImpressionadora.models import Post

#with app.app_context():
#    database.create_all()

# with app.app_context():
#     usuario = Usuario(username="Pedro", email="pedro@gmail.com", senha="123456")
#     usuario2 = Usuario(username="Joao", email="joao@gmail.com", senha="123456")
#
#     database.session.add(usuario)
#     database.session.add(usuario2)
#     database.session.commit()

# with app.app_context():
#     meus_usuarios = Usuario.query.all()
#     print(meus_usuarios)
#     primeiro_usuario = Usuario.query.first()
#     print(primeiro_usuario  .id)
#     print(primeiro_usuario.senha)
#     print(primeiro_usuario.posts)

# with app.app_context():
#     meu_post = Post(id_usuario=1, titulo="primeiro post do lira", corpo="lira voando")
#     database.session.add(meu_post)
#     database.session.commit()

# with app.app_context():
#     post = Post.query.first()
#     print(post.titulo)
#     print(post.autor.email)

# with app.app_context():
#     database.drop_all()
#     database.create_all()

# with app.app_context():
#     meus_usuarios = Usuario.query.all()
#     print(meus_usuarios)
#     primeiro_usuario = Usuario.query.first()
#     print(primeiro_usuario.id)
#     print(primeiro_usuario.email)
#     print(primeiro_usuario.senha)
#     print(primeiro_usuario.posts)
#     segundo_usuario = Usuario.query.filter_by(username='pedroc').first()
#     print(segundo_usuario.email)
#     print(segundo_usuario.senha)
#     database.drop_all()

# with app.app_context():
#     database.drop_all()
#     database.create_all()

# with app.app_context():
#     meus_usuarios = Usuario.query.all()
#     print(meus_usuarios)
#     primeiro_usuario = Usuario.query.first()
#     print(primeiro_usuario.id)
#     usuario = Usuario.query.filter_by(email='pedroteste@gmail.com').first()
#     usuario.cursos
#     print(usuario.cursos)

# with app.app_context():
#     meus_posts = Post.query.all()
#     print(meus_posts)
#     primeiro_post = Post.query.first()
#     primeiro_post.titulo
#     primeiro_post.corpo
#     print(primeiro_post.titulo)
#     print(primeiro_post.corpo)



