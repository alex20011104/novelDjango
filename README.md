这是微信小说系统的后端系统，提供了api接口和推荐算法。

static里面是爬虫代码和推荐算法，PC1是最新的爬小说章节并把数据插入数据库的代码，Pnovel是爬小说详情的代码，是爬取小说排行榜前五页的小说（大概有100本小说），具体可以在page_count变量中设置。

其中PC1.py的代码在api中的admin.py文件中被使用，主要是用于在后端小说管理界面中小说后面的爬取按钮，点击爬取后就会搜索数据库里面对应小说的url，开始爬取小说章节。

commend.py中的代码在view.py被使用，主要是用于在用户点击推荐后，系统会实时计算用户曾经的评分，根据算法推荐最有可能喜欢的小说，然后降序排列。其实应该在commend封装好然后在view中被调用，但是当时时间匆忙没有这样做。

在算法方面，是根据所有用户的评分，建立其一个关于皮尔逊相关系数的小说相似度矩阵，然后为每个用户通过他们的历史评分，进行相似度加权计算最后得出他们的最有可能的喜欢的小说。

微信小说阅读前端项目：https://github.com/alex20011104/novelwechat.git
