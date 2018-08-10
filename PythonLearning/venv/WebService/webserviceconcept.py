# 【web service 简介】
#
# 是一种新的web应用程序分支，是自包含、自描述、模块化的应用，可以发布、定位、通过web调用。web service是一个应用组件，它逻辑性的为其他应用程序提供数据与服务。各应用程序通过网络协议和规定的一些标准数据格式（HTTP，XML，SOAP）来访问web servcie，通过web servcie内部执行得到所需结果。
#
# web services ，可以将应用程序面向全世界发布，或提供某项功能，web services可以被其他应用程序使用。
#
#
#
# 【关键技术】
#
# （1）xml：描述数据的标准方法，web servcies使用xml来编解码数据
#
# xml提供了一种可用于不同的平台和编程语言之间的语言。
#
#
#
# （2）soap：表述信息交换的协议，web services使用saop来传输数据
#
# soap是一种用于访问web service的协议。
#
#
#
# （3）WSDL：web服务描述语言
#
# 使用XML编写，用于描述web services、如何访问web services以及用于web services的消息格式和协议的细节语言。
#
# （4）UDDI（Universal Description，Discovery and Integration）：通用描述、发现与集成，它是一种独立于平台的，基于xml语言的用于在互联网上描述商务的协议。
#
# 用户存储有关web services的信息的目录，经由SOAP进行通讯。
#
#
#
#
#
# 【web service通信】
#
# 不管web service用什么工具，什么语言写出来的，只要你用soap协议通过http来调用它，总体结构都一致。
#
# （1）用你喜欢的语言（如ＶＢ６或者ＶＢ.NET）来构建你的web services，然后用soap Toolkit或者.net的内建来把它暴漏给web客户。
#
# 注意：web service一般都是放在web服务器（如:IIS、tomcat）后面的。
#
# （2）任何语言、任务平台上的客户都可以阅读其WSDL文件来调用webservice。
#
#
#
# 【web service调用过程】
#
# （1）服务器端：生成服务描述文件，以供客户端获取（WSDL）。
#
# （1）客户端：取得服务端得服务描述文件WSDL，解析该文件的内容，了解服务端得服务信息以及调用方式。根据需要，生成恰当的SOAP请求消息（指定调用的方法，已经调用的参数），客户端生成的soap请求会被嵌入在一个HTTP POST请求中，发送到web服务器端。（之后，开始等待服务端返回的SOAP回应消息，解析得到返回值。）
#
# （2）web服务器端收到客户端的HTTP POST（SOAP）请求后，在将这些请求发给web service请求处理器。
#
# （3）web service请求处理器解析收到的soap请求消息，解析其中的方法调用和参数格式。根据WSDL和WSML的描述，调用相应的COM对象来完成制定功能，并把返回值放入SOAP回应消息中，传给web服务器端。
#
# （4）web服务器端得到soap应答后，会再通过HTTP应答的方式把它送回客户端。
#
#
#
# 【web service 调用实现】
#
# 1、高层接口
#
# 使用高层接口，不需要知道soap和xml的任何信息，就可以生成和使用一个webservice。soap Toolkit2.0通过提供两个com对象—soapClient和SoapServer，来完成这些功能。
#
# 在客户端，只要生成一个soapclient实例，并用WSDL作为参数来调用其中的mossoapinit方法。soapclient对象会自动解析WSDL文件，并在内部生成所有web service的方法和参数信息。之后，你就可以像调用IDispatch接口里的方法一样，调用里面所有的方法。在VB或是脚本语言中，你甚至可以直接在soapclient对象后面直接加上.方法（参数...）进行调用。
#
#
#
# 2、低层接口
#
# 要使用低层接口，你必须对soap和xml有所了解。你可以对soap的处理过程进行控制，特别是要做特殊处理的时候。
#
# 在客户端，首先要创建一个HTTPConnector队形，负责HTTP连接。设定connector的一些头部信息，比对EndPoinURL和SoapAction等。如果网络连接需要使用代理服务器，那页要在这里色设定相关的信息。接着创建SoapSerializer对象，用于生成soap消息。按照WSDL里定义，把所有参数按顺序序列化，得到一个完整的soap请求消息。该soap消息，作为payload通过Httpconnector被发送到服务器端。最后，生成一个soapreader对象，负责读取服务器端返回的soap消息，取得其中的返回值。