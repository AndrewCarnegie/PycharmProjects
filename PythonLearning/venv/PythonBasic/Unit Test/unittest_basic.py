# Python单元测试总结
#
# 1. 单元测试是什么？
# 单元测试（又称为模块测试, Unit Testing）是针对程序模块（软件设计的最小单位）来进行正确性检验的测试工作。程序单元是应用的最小可测试部件。在过程化编程中，一个单元就是单个程序、函数、过程等；对于面向对象编程，最小单元就是方法，包括基类（超类）、抽象类、或者派生类（子类）中的方法。单元测试粒度最小，一般由开发人员采用白盒方式来测试，主要测试单元是否符合设计。单元测试的主要过程仍是通过给定的输入，判断得到的结果是否符合预期的代码结果测试的过程。
#
# 2. 为什么需要单元测试
# 总的来说，单元测试有以下好处：
#
# •确保代码质量
#
# •改善代码设计，难以测试的代码一般是设计不够简洁的代码。
#
# •保证重构不会引入新问题，以函数为单位进行重构的时候，只需要重新跑测试就基本可以保证重构没引入新问题
#
# •通过单元测试，可以增强代码的执行与预期一致，增强对于代码的自信。
#
# •在测试驱动编程的理念中，首先程序员要编写测试程序，然后编写可以通过测试的程序。测试程序就是程序的需求说明，它能够帮助程序员在开发程序时，不偏离需求。TTD[Test-Driven Development]最大的好处就是确保一个程序模块的行为符合我们设计的测试用例。
#
# 3. 怎么编写单元测试
# 对于Python代码而言，常用的测试工具有doctest和unittest，doctest是简单一些的模块，是检测文档用的。doctet.test_mod函数从一个模块中读取所有文档字符串，找出所有看起来像是在交互式解释器中输入的例子的文本，之后检查例子是否符合实际要求。
#
# 3.1doctest
# 定义如下函数代码square，求一个数的平凡，并且在它的文档字符串中添加两个例子，文件名为my_math.py
#
# <textarea readonly="readonly" name="code" class="python">
# #!/usr/bin/python
# import doctest
# def square(x):
#     '''
#     Squares a number and returns the result
#
#     >>> square(2)
#     4
#     >>> square(3)
#     9
#     '''
#     return x*x
# if __name__ == '__main__':
#     import my_math
#     doctest.testmod(my_math)
# </textarea>
#
#
#
#
# 上述my_math.py文件，是较为标准的文档字符串格式，诸如>>>后有一个空格，’’’后的英文文档后有一个空行。
#
# 之后我们可以在Linux命令行中运行查看测试结果。
# [root@centos ~]#python my_math.py
#
# [root@centos ~]#python my_math.py -v
#
# Trying:
#
# square(2)
#
# Expecting:
#
# 4
#
# ok
#
# Trying:
#
# square(3)
#
# Expecting:
#
# 9
#
# ok
#
# 1 items had notests:
#
# my_math
#
# 1 items passedall tests:
#
# 2 tests in my_math.square
#
# 2 tests in 2items.
#
# 2 passed and 0failed.
#
# Test passed.
#
# 3.2unittest
# 在实际工作中，为python写单元测试时更加强大和常用的模块是unittest模块，unittest基于Java的流行测试框架Junit，通过使用unittest我们可以以结构化的方式编写大型而且周详的测试集。Unittest文件位置在/usr/lib64/python2.7/unittest/__init__.pyc。unittest框架的主要组成部分
#
# >>> dir(unittest)
#
# ['BaseTestSuite','FunctionTestCase', 'SkipTest','TestCase','TestLoader', 'TestProgram', 'TestResult','TestSuite','TextTestResult','TextTestRunner', '_TextTestResult', '__all__','__builtins__', '__doc__', '__file__', '__name__', '__package__', '__path__','__unittest', '_expectedFailureInRpmBuild', '_skipInRpmBuild', 'case','defaultTestLoader', 'expectedFailure', 'findTestCases', 'getTestCaseNames','installHandler', 'loader', 'main', 'makeSuite', 'registerResult','removeHandler', 'removeResult', 'result', 'runner', 'signals', 'skip','skipIf', 'skipUnless', 'suite', 'util']
#
# 如下所示：
#
# TestCase 测试用例
#
# 所有测试用例类继承的基本类。测试行为的最小单位，通过对一些输入输出值的对比来进行测试检查。
#
# TestLoader  测试加载器
# TestLoader负责根据各种各样的规则收集测试用例，并把这些测试用例包装在一个TestSuite中。
#
# TestSuite  测试套件
# 组织测试用例的实例，支持测试用例的添加和删除，最终将传递给 testRunner进行测试执行。一个test suite由许多个TestCase组成，常见的情形是创建一个TestSuite的实例，然后向TestSuite实例添加测试用例TestCase实例，当所有测试添加之后，可以把TestSuite的实例传递给TextTestRunner，它会按照添加测试用例的顺序逐个去执行测试用例，并手机测试结果
#
# TextTestRunner
#
# 一个test runner类会以文本的形式显示结果，在它们运行时会打印测试名字，发生的错误，并且在测试运行结束之后打印结果概要。将测试用例或测试用例集合聚合起来的集合，批量执行。
#
# TextTestResult
# 由TextTestRunner调用，会显示出格式化的文本。
#
# 4. unittest模块
# unittest模块使用的模式有三种，如下：
#
#
#
# 4.1通过unittest.main()来执行测试用例的方式：
# import unittest
#
# class UCTestCase(unittest.TestCase):
#     def setUp(self):
#         #测试前需执行的操作
#         .....
#     def tearDown(self):
#
#         #测试用例执行完后所需执行的操作
#         .....
#
#         #测试用例1
#     def testCreateFolder(self):
#
#         #具体的测试脚本
#         ......
#
#     #测试用例2
#
#     deftestDeleteFolder(self):
#
#     #具体的测试脚本
#
#     ......
#
# if __name__ == "__main__":
#
# unittest.main()
#
#
#
# 4.2通过testsuit来执行测试用例的方式：
# import unittest
# # 执行测试的类
# class UCTestCase(unittest.TestCase):
#     def setUp(self):
#         #测试前需执行的操作
#         .....
#     def tearDown(self):
#         #测试用例执行完后所需执行的操作
#         .....
#
#     #测试用例1
#     def testCreateFolder(self):
#         #具体的测试脚本
#         ......
#
# deftestDeleteFolder(self):
#
# #具体的测试脚本
#
# If __name__ =="__main__":
#
# #构造测试集， 添加测试用例
#
# suite = unittest.TestSuite()
#
# suite.addTest(UC7TestCase("testCreateFolder"))
#
# suite.addTest(UC7TestCase("testDeleteFolder"))
#
# #执行测试， 构造runner。
#
# runner= unittest.TextTestRunner()
#
# runner.run(suite)
#
#
#
# 4.3通过testloader运行测试集
# import unittest
#
# classTestCase1(unittest.TestCase):
#
# #def setUp(self):
#
# #def tearDown(self):
#
# def testCase1(self):
#
#     print 'aaa'
#
# def testCase2(self):
#
#     print 'bbb'
#
# classTestCase2(unittest.TestCase):
#
# #def setUp(self):
#
# #def tearDown(self):
#
# def testCase1(self):
#
#     print 'aaa1'
#
# def testCase2(self):
#
#     print 'bbb1'
#
#
#
# if __name__ == "__main__":
#
# #此用法可以同时测试多个类
#
# suite1=unittest.TestLoader().loadTestsFromTestCase(TestCase1)
#
# suite2=unittest.TestLoader().loadTestsFromTestCase(TestCase2)
#
# suite = unittest.TestSuite([suite1, suite2])
#
# unittest.TextTestRunner(verbosity=2).run(suite)
#
# 5. TestCase的用法
# 源文件widget.py，也即我们要进行单元测试的文件。很简单的一个类，该类可以设置长宽，并且能够获取这两个值。
#
#
# 因此，我们可以撰写的单元测试代码文件widgettest.py如下：
#
# 其中有两个测试用例，分别为test_size,test_Resize， 在每个测试用例执行的过程中会首先执行setUp，然后执行测试用例，最后执行tearDown操作。每个测试用例的执行遵循相同的模式。
#
# 其中要注意的是setUp和tearDown两个，又称为测试装置，setUp完成对象的初始化动作，而tearDown则完成资源的释放之类的操作。
#
# 在实际工作中，最常见的实践仍是写一个测试类继承自unittest.TestCase，然后让每一个测试用例名称以test开头，在运行测试集合时使用unittest.main（）函数即可。自动化测试便是建立在这样的基础上。
#
# 6. Mock和MagicMock
# 在单元测试进行的同时，就离不开mock模块的存在，初次接触这个概念的时候会有这样的疑问：把要测的东西都模拟掉了还测试什么呢？
#
# 　　但在，实际生产中的项目是非常复杂的，对其进行单元测试的时候，会遇到以下问题：
#
# •接口的依赖
#
# •外部接口调用
#
# •测试环境非常复杂
#
# 单元测试应该只针对当前单元进行测试,所有的内部或外部的依赖应该是稳定的,已经在别处进行测试过的.使用mock就可以对外部依赖组件实现进行模拟并且替换掉,从而使得单元测试将焦点只放在当前的单元功能。
#
#
# 因为在为代码进行单元测试的同时，会发现该模块依赖于其他的模块，例如数据库，网络，或者第三方模块的存在，而我们对一个模块进行单元测试的目的，是测试当前模块正常工作，这样就要避开对其他模块的依赖，而mock主要作用便在于，专注于待测试的代码。而在但与测试中，如何灵活的使用mock模块是核心所在。下面便以mock为核心，结合最近所写的代码，阐述mock模块的使用。
#
#
#
# 7. mock模块的使用
# 在mock模块中，两个常用的类型为Mock，MagicMock，两个类的关系是MagicMock继承自Mock，最重要的两个属性是return_value, side_effect。
#
# >>> from mock import Mock
#
# >>> fake_obj = Mock()
#
# >>>fake_obj.return_value ='This is a mock object'
#
# >>> fake_obj()
#
# 'This is a mock object'
#
# 我们通过Mock()可以创建一个mock对象，通过renturn_value指定它的返回值。即当下文出现fake_obj()会返回其return_value所指定的值。
#
# 也可以通过side_effect指定它的副作用，这个副作用就是当你调用这个mock对象是会调用的函数,也可以选择抛出一个异常，来对程序的错误状态进行测试。
#
# >>>def b():
#
# ...   print 'This is b'
#
# ...
#
# >>>fake_obj.side_effect = b
#
# >>>fake_obj()
#
# This is b
#
# >>>fake_obj.side_effect = KeyError('This is b')
#
# >>>fake_obj()
#
# ...
#
# KeyError: 'This is b'
#
# 如果要模拟一个对象而不是函数，你可以直接在mock对象上添加属性和方法，并且每一个添加的属性都是一个mock对象【注意，这种方式很有用】，也就是说可以对这些属性进行配置,并且可以一直递归的定义下去。
#
# >>>fake_obj.fake_a.return_value= 'This is fake_obj.fake_a'
#
# >>>fake_obj.fake_a()
#
# 'This is fake_obj.fake_a'
#
# 上述代码片段中fake_obj是一个mock对象，而fake_obj.fake_a的这种形式使得fake_a变成了fake_obj的一个属性，作用是在fake_obj.fake_a()调用时会返回其return_value。
#
# 另外也可以通过为side_effect指定一个列表，这样在每次调用时会依次返回，如下：
#
# >>>fake_obj = Mock(side_effect = [1, 2, 3])
#
# >>>fake_obj()
#
# 1
#
# >>>fake_obj()
#
# 2
#
# >>>fake_obj()
#
# 3
#
#
#
#
#
#
#
# 7.1函数的如何mock
# 在rbd_api.py文件中如下内容：
#
#
# 要为这个函数撰写单元测试，因为其有数据库的操作，因而就需要mock出DAO_query_ispoolok操作。
#
# 因此，我们在test_rbd_api.py文件中可以这么写：因为DAO_query_ispoolok是类DAO_PoolMgr的操作，因此可以这么写
#
#
# 测试用例上的装饰器含义如下：
#
# @mock.pathc.object(类名，“类中函数名”)，而如果想要忽略某个测试用例，则可以通过装饰器@unittest.skip(“原因”)
#
# 而对于另外一种情形则是在另外一个函数中调用了checkpoolstat函数。
#
# 如下rbd_api.py：
#
# def checkpoolstat():
#
#     ……
#
#
#
#     class Disk(Resource):
#
#         def __init__(self):
#
#             ……
#
#             def delete(self, pool, img):
#
#                 ret = rbd_api.checkpoolstat()
#
#                 ……
#
#             这样，我们在为delete函数撰写单元测试时，也可以在test_rbd_api.py中使用如下的方式：
#
#             import rbd_api
#
#
#
#             class TestDisk(unittest.TestCase):
#
#                 def setup():
#
#                     …
#
#                 def teardown():
#
#                     …
#
#                 @mock.patch(“rbd_api.checkpoolstat”, Mock(return_value= True))
#
#                 def test_delete():
#
#                     # rbd_api.checkpoolstat 已经成为一个mock对象了，调用时返回True
#
#                     …
#
#             此时的装饰器应该为
#
#             @mock.patch(“模块名.函数名”)
#
#             7.2链式函数抛出异常
#             在rbd_api.py文件中，有一行代码如下：
#
#             ret = OpRBD(pool).flatten(img)
#
#             类似这种链式调用的，在前一个函数中抛出异常，要怎么写？如下：
#
#             rbdServ.OpRBD = MagicMock()
#
#             rbdServ.OpRBD(pool).side_effect = rados.Error(“Error: errorconnecting to the cluster: error code 24”)
#
#
#
#             7.3全局函数如何mock
#             例如在文件rbd_api.py中有全局函数checkpoolstat(pool)，它是一个全局函数，这样在进行单元测试的过程中，我们可能需要mock该函数。该函数的具体代码如下：
#
#
#             因此，我们在test_rbd_api.py文件中为该函数撰写单元测试，可以这么做。
#
#             在文件开始处导入该rbd_api模块。
#
#             import rbd_api as rbdAPI
#
#             deftest_patchInvalid_Parameter(self):
#
#             ……
#
#             rbdAPI.checkpoolstat.return_value= MGR_COMMON.POOL_STAT_ERROR
#
#             即可。
#
#         7.4链式调用正常
#         在rbd_api文件中有如下代码行：
#
#         ret =OpRBD(pool).flatten(img)
#
#         在第一个函数未出现异常，在flatten函数中返回值可以在test_rbd_api.py文件中如下写代码：
#
#         rbdServ.OpRBD(pool).snap_rollback =MagicMock(return_value = RBD_COMMON.CODE_EXEC_SUCCESS_MODIFY)
#
#         7.5with子句mock
#         #!/usr/bin/python
#
#         import rados
#
#         class OpRBD:
#
#             def__init__(self):
#
#             ...
#
#
#
#         def__del__(self):
#
#         ...
#
#
#
#     def resize(self, img, size):
#
#         try:
#
#             withrbd.Image(self.ioctx, img) as image:
#
#             ifimage.size() < size:
#
#             image.resize(size)
#
#         else:
#
#         returnRBD_COMMON.CODE_ARGUMENT_LESS_THAN_ORIGINAL
#
# exceptrbd.ImageNotFound as exce1
#
# print(exce1)
#
# return RBD_COMMON.CODE_IMAGE_NOT_FOUND
#
# 由于是在with子句中要进行mock，在此简单的对with的知识点进行说明：
#
# 要使用 with语句，首先要明白上下文管理器这一概念。有了上下文管理器，with语句才能工作。
#
# 下面是一组与上下文管理器和with语句有关的概念。
#
# 上下文管理协议（ContextManagement Protocol）：包含方法 __enter__()和 __exit__()，支持
#
# 该协议的对象要实现这两个方法。
#
# 上下文管理器（ContextManager）：支持上下文管理协议的对象，这种对象实现了__enter__()和 __exit__() 方法。上下文管理器定义执行 with语句时要建立的运行时上下文，
#
# 负责执行 with语句块上下文中的进入与退出操作。通常使用 with语句调用上下文管理器，也可以通过直接调用其方法来使用。
#
# 运行时上下文（runtime context）：由上下文管理器创建，通过上下文管理器的__enter__()和__exit__()方法实现，__enter__()方法在语句体执行之前进入运行时上下文，__exit__()在语句体执行完后从运行时上下文退出。with语句支持运行时上下文这一概念。
#
# 上下文表达式（ContextExpression）：with语句中跟在关键字 with之后的表达式，该表达式要返回一个上下文管理器对象。
#
# 语句体（with-body）：with语句包裹起来的代码块，在执行语句体之前会调用上下文管理器的__enter__()方法，执行完语句体之后会执行 __exit__() 方法。
#
# 出现异常时，如果 __exit__(type, value, traceback)返回 False，则会重新抛出异常，让with之外的语句逻辑来处理异常，这也是通用做法；如果返回 True，则忽略异常，不再对异常进行处理。因此，在对with子句进行mock时，要具有两个函数，__exit__,__enter__，并且如果在with语句体重抛出异常并被with之外的代码进行捕获异常，要使得__exit__返回False，因此可以撰写测试代码如下：
#
# #!/usr/bin/python
#
# import rados
#
# class OpRBD:
#
#     def __init__(self):
#
#         ...
#
#
#
#     def__del__(self):
#
#     ...
#
#
#
# defresize(self, img, size):
#
# try:
#
#     withrbd.Image(self.ioctx, img) as image:
#
#     ifimage.size() < size:
#
#     image.resize(size)
#
# else:
#
# returnRBD_COMMON.CODE_ARGUMENT_LESS_THAN_ORIGINAL
#
# exceptrbd.ImageNotFound as exce1
#
# print(exce1)
#
# return RBD_COMMON.CODE_IMAGE_NOT_FOUND
#
# class TestOpRBD(unittest.TestCase):
#
#     defsetUp(self):
#
#     ...
#
# deftearDown(self):
#
# ...
#
# deftest_resize(self):
#
# fake_image = Mock()
#
# fake_image.__enter__ = Mock(return_value = fake_image)
#
# fake_image.__exit__ = Mock(return_value = True)
#
# rbd.Image = Mock(return_value = fake_image)
#
# size= 1073741824L / 2
#
# fake_image.size= Mock(return_value = 1073741824L)
#
# fake_image.resize= Mock(return_value = None)
#
# self.assertEqual(self.opRBD.resize(self.img,size), RBD_COMMON.CODE_ARGUMENT_LESS_THAN_ORIGINAL)
#
#
#
# size= 2 * 1073741824L
#
# self.assertEqual(self.opRBD.resize(self.img,size), RBD_COMMON.CODE_EXEC_SUCCESS_MODIFY)
#
# rbd.Image= Mock(side_effect = rbd.ImageNotFound("%s image not found!"%self.img))
#
# self.assertEqual(self.resize(self.img,size), RBD_COMMON.CODE_IMAGE_NOT_FOUND)
#
#
#
# 7.6连续mock
# 在rbd_api文件中有一个OpRados类的内容如下：
#
# #!/usr/bin/python
#
# import rados
#
#
#
# class OpRados:
#
#     def __init__(self):
#
#         self.cluster = rados.Rados(conffile=rconf['conffile'])
#
#         self.cluster.connect()
#
#
#
#     def __del__(self):
#
#         self.cluster.shutdown()
#
#
#
#     def lists(self):
#
#         returnutil.return_format(RBD_COMMON.CODE_EXEC_SUCCESS_GET, "",self.cluster.list_pools())
#
# 为该类写单元测试，具体代码如下：
#
# #!/usr/bin/python
#
# import rados
#
# import unittest
#
# from mock import Mock
#
# class TestOpRados(unittest.TestCase):
#
#     def setUp(self)：
#
#     fake_Rados = Mock()
#
#     fake_Rados.connect =Mock(return_value = None)
#
#     fake_Rados.shutdown =Mock(return_value = None)
#
#     fake_Rados.list_pools= Mock(return_value = ["sqh", "sqh1"])
#
#     #注意：此处要使得rados.Rados()调用返回fake_Rados.
#
#     #如果写成rados.Rados = fake_Rados,只能使得self.cluster重新生成一个Mock对象
#
#     #无法有效的控制为fake_Rados所添加的属性。
#
#     rados.Rados =Mock(return_value = fake_Rados)
#
#     self.opRados =OpRados()
#
#
#
# def tearDown(self):
#
#     fake_Rados = None
#
#     self.opRados = None
#
#
#
# def test_list(self):
#
#     return_list =["sqh", "sqh1"]
#
#     self.assertEqual(self.opRados.lists(),
#
#                      util.return_format(RBD_COMMON.CODE_EXEC_SUCCESS_GET,
#
#                                         "", return_list))
#
# 7.7Flask API接口的模拟调用
# 有三个文件：rbd_app.py文件内容如下：
#
# #!/usr/bin/python
#
# from flask imort Flask
#
# from flask.ext import restful
#
#
#
# app = Flask(__name__)
#
# api = restful.Api(app)
#
#
#
# api_version = "/v1.0"
#
# ##
#
# ## Actually setup the Api resource ruting here
#
# ##
#
#
#
# ...
#
# api.add_resource(rbd_api.Disk,api_version+"pools/<pool>/disks/<img>")
#
# ...
#
#
#
# if __name__ == __main__:
#
#     fromgevent.wsgi import WSGIServer
#
#     http_server= WSGIServer(('0.0.0.0', 4806), app)
#
#     http_server.serve_forever()
#
#
#
# rbd_api.py文件中Disk类内容如下：
#
# #!/usr/bin/python
#
# import requests
#
# from flask import request
#
# from flask_restful import reqparse, Resource
#
#
#
#
#
# class Disk(Resource):
#
#     defget(self, pool, img):
#
#     ret,rbd_info = DAO_query_rbd_info(pool, img)
#
#     ...
#
#
#
# defpost(self, pool, img):
#
# parser= reqparser.RequestParser()
#
# #action: create\copy\clone
#
# parser.add_argument('action',type=str)
#
# parser.add_argument('src_pool',type=str)
#
# parser.add_argument('src_rbd',type=str)
#
# parser.add_argument('src_snap',type=str)
#
# parser.add_argument('size',type=str)
#
# parser.add_argument('unit',type=str)
#
#
#
# action= args.get('action')
#
# ifaction == "create":
#
# size= args.get('size')
#
# unit= args.get('unit')
#
# ...
#
# elifaction == 'copy':
#
# src_pool= args.get('src_pool')
#
# src_rbd= args.get('src_rbd')
#
# ...
#
# else
#
# return...
#
#
#
# defdelete(self, pool, img):
#
# ...
#
#
#
# defput(self, pool, img):
#
# parser= reqparser.RequestParser()
#
# parser.add_argument('rb_snap',type=str)
#
# parser.add_argument('action',type=str)
#
# args= parser.parse_args()
#
#
#
# ifaction == "flatten":
#
# ...
#
# elifaction == "rollback":
#
# snap= args.get("rb_snap")
#
# ...
#
# else:
#
# return...
#
#
#
# defpatch(self, pool, img):
#
# parser= reqparse.RequestParser()
#
# parser.add_argument("action",type=srt)
#
# parser.add_argument("name",type=str)
#
# parser.add_argument("size",type=float)
#
# parser.add_argument("unit",type=str)
#
# args= parser.parse_args()
#
# action= args.get('action')
#
# ifaction == "resize":
#
# size= args.get('size')
#
# unit= args.get('unit')
#
# ....
#
# else:
#
# return...
#
# 在test_rbd_api.py中卫Disk类撰写单元测试
#
# from rbd_app import app
#
#
#
# class TestDisk(uniitest.TestCase):
#
#     defsetUp(self):
#
#     self.disk= Disk()
#
#     self.content_type= "application/json"
#
#     ...
#
#
#
# deftearDown(self):
#
# self.disk= None
#
# self.content_type= None
#
# ...
#
#
#
# @mock.path.object(DAO_RBDMgr,"DAO_query_rbd_info")
#
# deftest_get(self, mock_DAO_query_rbd_info):
#
# rbd_info= {"pool_name":"sqh", "parent":{},"image_size":1073741824L,...}
#
# mock_DAO_query_rbd_info.return_value= (RBD_COMMON.MONGO_SUCCESS, rbd_info)
#
#
#
# withapp.test_request_context("/?pool_name=sqh&image_name=sqh001"):
#
# pool= request.args.get('pool_name')
#
# img=request.args.get('image_name')
#
# self.assertEqual(selff.disk.get(pool,img), RBD_COMMON.http_return(RBD_COMMON.MONGO_SUCCESS))
#
#
#
#
#
# deftest_post(self):
#
# pool= "sqh"
#
# img= "sqh001"
#
# path_url= "v1.0/pools/%s/disks%s" % (pool, img)
#
# data= {"action":"create", "size":2,"unit":"GB"}
#
# withapp.test_request_context(path_url, data=json.dumps(data),content_type=self.content_type):
#
# self.assertEqual(self.disk.post(pool,img), RBD_COMMON.http_return(RBD_COMMON.CODE_EXEC_SUCCESS_GET))
#
#
#
# deftest_delete(self):
#
# pool= "sqh"
#
# img= "sqh001"
#
# path_url= "v1.0/pools/%s/disks%s" % (pool, img)
#
# withapp.test_request_context(path_url):
#
# self.assertEqual(self.disk.delete(pool,img), RBD_COMMON.http_return(RBD_COMMON.CODE_EXEC_SUCCESS_DELETE))
#
#
#
# deftest_put(self):
#
# pool= "sqh"
#
# img= "sqh001"
#
# path_url= "v1.0/pools/%s/disks%s" % (pool, img)
#
# data= {"action":"rollback", "rb_snap":"sqh_snap"}
#
# withapp.test_request_context(path_url, data=json.dumps(data),content_type=self.content_type):
#
# self.assertEqual(self.disk.put(pool,img), RBD_COMMON.http_return(RBD_COMMON.CODE_EXEC_SUCCESS_FLATTENING))
#
#
#
# deftest_patch(self):
#
# pool= "sqh"
#
# img= "sqh001"
#
# path_url= 'v1.0/pools/%s/disks/%s' %　(pool, img)
#
# size= 1073741824L
#
# data= {"action":"resize", "size":size,"unit":"GB"}
#
# #the action resize
#
# withapp.test_request_context(path_url, data=json.dumps(data), content_type=self.content_type):
#
# self.assertEqual(self.disk.patch(pool,img), RBD_COMMON.http_return(RBD_COMMON.CODE_EXEC_SUCCESS_MODIFY))
#
# 7.7.1   Get请求
# @mock.path.object(DAO_RBDMgr,"DAO_query_rbd_info")
#
# deftest_get(self, mock_DAO_query_rbd_info):
#
# rbd_info= {"pool_name":"sqh", "parent":{},"image_size":1073741824L,...}
#
# mock_DAO_query_rbd_info.return_value= (RBD_COMMON.MONGO_SUCCESS, rbd_info)
#
#
#
# withapp.test_request_context("/?pool_name=sqh&image_name=sqh001"):
#
# pool= request.args.get('pool_name')
#
# img=request.args.get('image_name')
#
# self.assertEqual(selff.disk.get(pool,img), RBD_COMMON.http_return(RBD_COMMON.MONGO_SUCCESS))
#
#
#
# 在为flask接口撰写单元测试时，最关键的是如何传递数据，
#
# 我们在setUp函数中初始化Disk类的实例,即self.disk。在传递参数的时候通过调用app.test_request_context(“url”)。因为是restful的get请求，因而我们可以使用？param1=val1&param2=val2的形式。
#
# 7.7.2   Post请求
# 在Post请求，我们需要传递动作的类型，即其他参数，在app.test_request_context函数中，传递了字符串url， data字典，HTTP请求头信息。
#
# def test_post(self):
#
#     pool= "sqh"
#
#     img= "sqh001"
#
#     path_url= "v1.0/pools/%s/disks%s" % (pool, img)
#
#     data= {"action":"create", "size":2,"unit":"GB"}
#
#     withapp.test_request_context(path_url, data=json.dumps(data),content_type=self.content_type):
#
#     self.assertEqual(self.disk.post(pool,img), RBD_COMMON.http_return(RBD_COMMON.CODE_EXEC_SUCCESS_GET))
#
#
#
# 7.7.3   Delete请求
# 如post
#
# 7.7.4   Put请求
# 如post
#
# 7.7.5   Patch请求
# 如post
#
#
#
# 8. Python单元测试环境安装
# 因为在python2.*中，mock是单独的模块，因而我们需要单独安装mock模块才能够正常的使用。
#
# 因此，我们首先要在rpm find网站下载好pip，然后通过pip安装mock。
#
# http://rpmfind.net/linux/RPM/epel/7/x86_64/Packages/p/python2-pip-8.1.2-5.el7.noarch.html
#
# 依赖于python-setuptools
#
# http://rpmfind.net/linux/RPM/centos/7.4.1708/x86_64/Packages/python-setuptools-0.9.8-7.el7.noarch.html
#
# mock的下载网址：
#
# https://pypi.python.org/pypi/mock/2.0.0
#
# 下一章节要用的coverage，测试代码覆盖率，网址在：
#
# https://pypi.python.org/pypi/coverage/4.5.1
#
#
#
# 9. 使用coverage测试覆盖率
# 在单元测试的过程中，应尽量使得单元都被覆盖过，因而需要使用专门的工具来进行测试代码覆盖率。以test_rbd_api.py为准
#
# 测试的步骤如下：
#
# >>>coverage run test_rbd_api.py
#
# >>>coveragereport -m path/to/rbd_api.py
#
# 即可查看代码覆盖程度。