# 用户发表文章
# 创建用户对象
from article.models import Article
from user.models import User
# from .models import User # 当前目录下的models里面的User类

u = User('雨行', '123456')

# 发表文章，文章对象   # -----> user就是通过导入User类创建的

a = Article('三国演绎', '罗贯中')
u.publish_article(a)

