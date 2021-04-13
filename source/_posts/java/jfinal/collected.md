---
title: 'jFinal配置自动生成'
cover: "/img/lynk/68.jpg"
date:       2021-04-10
tags:
	- Java
	- jFinal
	
---
  
  

  
  
  
  




<body>
<h1>JDBC 03</h1>
<p>2019/8/1 9:51:41 </p>
<hr />
<h3>笔记网站</h3>
<pre><code>全球加速:   http://zaixianke.com
北京节点:   http://itdage.cn
</code></pre>

<h3>JDBC 事务 ***</h3>
<pre><code>在dos命令行操作oracle时 , 执行DML , 需要结束事务 (commit提交 或 rollback回退)
在JDBC中, 事务是自动提交的, 每执行一条DML语句, 事务就自动提交一次. 

我们可以通过JDBC的事务API , 开始事务的手动提交, 将多条DML语句看作一个整体, 要么一起成功, 要么一起失败.
</code></pre>

<h4>JDBC事务操作格式:</h4>
<pre><code>注意: 开启事务的手动提交 ,是通过连接对象完成的. 
        某个数据连接对象的事务开启手动提交后, 这个连接对象的事务需要手动控制.  其他连接对象不受影响.

操作方法:
    1.  开始事务的手动提交:
            conn.setAutoCommit(boolean flag);
            参数含义:   true表示自动提交 . false表示手动提交.

    2.  提交事务:
            conn.commit();

    3.  回退事务:
            rollback();
</code></pre>

<h4>事务案例:</h4>
<pre><code>    public class Demo {
    public static void main(String[] args) throws Exception {
        //1.    加载数据库的驱动
        Class.forName(&quot;oracle.jdbc.OracleDriver&quot;);
        //2.    获取数据库连接对象
        Connection conn = DriverManager.getConnection(&quot;jdbc:oracle:thin:@localhost:1521:XE&quot;, &quot;system&quot;, &quot;123&quot;);
        //2.1   设置连接对象的事务 为 手动提交
        conn.setAutoCommit(false);
        //3.    开始描述逻辑
        System.out.println(&quot;金刚: 转账中...&quot;);
        //3.1   减少金刚账户的余额 500 | 3.1.1   预编译SQL执行环境
        PreparedStatement state = conn.prepareStatement(&quot;update user33 set money=500 where id=2&quot;);
        //3.1.2 执行SQL语句
        boolean success = state.executeUpdate()&gt;0?true:false;
        if(success) {
            System.out.println(&quot;后台逻辑: 金刚余额减少完毕.&quot;);
            if(1==2) {
                conn.rollback();
                throw new RuntimeException(&quot;后台服务器... 停电了&quot;);
            }
            //3.2   增加豪杰账户的余额 500 
            //3.2.1 预编译SQL执行环境
            PreparedStatement state2 = conn.prepareStatement(&quot;update user33 set money=600 where id=1&quot;);
            //3.2.2 执行SQ语句
            boolean success2 = state2.executeUpdate()&gt;0?true:false;
            if(success2) {
                System.out.println(&quot;后台逻辑: 豪杰余额增加完毕&quot;);
                conn.commit();
            }
            state2.close();
        }
        state.close();
    }
}
</code></pre>

<h3>批处理 了解</h3>
<pre><code>将多条SQL语句 放到一起批量处理.

批处理将多次对于数据库的操作次数 , 减少到了一次 ! 提高了大量SQL语句一起执行时的性能.

使用步骤:

    批处理使用Statement类操作
        步骤1.    将一条SQ语句加入到批处理中
            statement.addBatch(String sql);

        步骤2.    执行批处理中的所有语句
            statement.executeBatch();
</code></pre>

<h4>批处理案例:</h4>
<pre><code>    //1.    加载数据库的驱动
    Class.forName(&quot;oracle.jdbc.OracleDriver&quot;);
    //2.    获取数据库连接对象
    Connection conn = DriverManager.getConnection(&quot;jdbc:oracle:thin:@localhost:1521:XE&quot;, 
            &quot;system&quot;, &quot;123&quot;);
    //3.    创建SQL的执行环境
    Statement state = conn.createStatement();
    //4.    加入SQL语句 到批处理中
    for(int i=0;i&lt;1000;i++) {
        state.addBatch(&quot;insert into user33 values(SEQ_USER33_ID.NEXTVAL,'name&quot;+i+&quot;',1000)&quot;);
    }
    //5.    执行批处理
    state.executeBatch();
    state.close();
    conn.close();
    System.out.println(&quot;执行完毕&quot;);
</code></pre>

<h3>连接池 *</h3>
<h4>概述 熟悉</h4>
<pre><code>由连接池创建连接, 维护连接 
我们需要使用连接时, 从连接池中获取连接. 
如果池中存在空闲连接, 则拿去使用. 
如果不存在空闲连接, 且池未满 , 则在连接池中创建新的连接使用.
如果不存在空闲连接, 且池已满 , 则排队等待空闲连接.
</code></pre>

<h4>Properties 文件 与 类 熟悉</h4>
<pre><code>properties文件 常用于Java中的配置文件.
因为Properties文件 可以快速的 与 Properties类 进行转换.    

文件:
    注释: #开头表示注释行
    键值对: 键与值之间使用等号连接,  多个键值对之间使用换行分割

如何将一个Properties文件, 转换为java中的Map集合对象:

    步骤:
        1.  创建Properties对象
            Properties ppt = new Properties();          
        2.  得到Properties文件的字节输入流
            InputStream is = //可以通过new FileInputStream , 也可以通过ClassLoader 等等
        3.  将流加载到Properties对象
            ppt.load(is);
</code></pre>

<h4>使用步骤: *</h4>
<pre><code>1.  引入相关的jar文件
        -   dbcp    :   连接池的代码
        -   poll    :   连接池的依赖库

2.  创建一个properties文件, 描述连接池的配置 , 内容如下:
    #数据库连接地址
    url=jdbc:oracle:thin:@localhost:1521:XE
    #数据库驱动地址
    driverClassName=oracle.jdbc.OracleDriver
    #数据库帐号
    username=system
    #数据库密码
    password=123

    #扩展配置:
    #初始化连接池时, 创建的连接数量:
    initialSize=5
    #最大允许存在的连接数量
    maxActive=200
    #空闲时允许保留的最大连接数量
    maxIdle=10
    #空闲时允许保留的最小连接数量
    minIdle=5
    #排队等候的超时时间
    maxWait=20000

3.  将properties文件, 转换为Properties对象.
    Properties ppt = new Properties();
    ppt.load(文件输入流);
4.  通过连接池工厂类(BasicDataSourceFactory) , 创建连接池对象 (一次程序启动, 创建一个连接池就够了.)
    DataSource ds = BasicDataSourceFactory.createDataSource(ppt);
5.  通过连接池对象, 获取池中的连接
    Connection conn = ds.getConnection();
6.  正常JDBC操作
</code></pre>

<h4>连接池案例:*</h4>
<pre><code>    //3.    将properties文件 转换为Properties对象
    Properties ppt = new Properties();
    //4.    加载文件的输入流
    InputStream is = Demo.class.getClassLoader().getResourceAsStream(&quot;dbcp.properties&quot;);
    //空指针异常
    ppt.load(is);
    //5.    通过工厂类, 创建连接池
    DataSource ds = BasicDataSourceFactory.createDataSource(ppt);
    //6.    通过连接池, 获取其中的连接 , 并使用
    Connection conn = ds.getConnection();
    //正常的JDBC操作
    PreparedStatement state = conn.prepareStatement
            (&quot;insert into user33 values(seq_user33_id.nextval,'嘿嘿嘿',188)&quot;);
    int count = state.executeUpdate();
    System.out.println(count&gt;0?&quot;数据插入成功&quot;:&quot;数据插入失败&quot;);
</code></pre>

<h4>DBCPUtil工具类 *</h4>
<pre><code>public class DBCPUtil {

    private static DataSource dataSource;

    static {
        //在类加载时, 读取配置文件, 配置连接池
        //1.    创建Properites对象
        Properties ppt = new Properties();
        //2.    读取配置文件, 
        InputStream is = DBCPUtil.class.getClassLoader().getResourceAsStream(&quot;dbcp.properties&quot;);
        //3.    将配置文件 加载到Properties对象中
        try {
            ppt.load(is);
        //4.    通过连接池工厂类, 创建连接池
            dataSource = BasicDataSourceFactory.createDataSource(ppt);
        } catch (Exception e) {
            e.printStackTrace();
        }
    }

    /**
     * 用于从连接池中 获取一个连接对象
     * @return 连接对象 , 如果获取失败返回null
     */
    public static Connection getConnection() {
        try {
            return dataSource.getConnection();
        } catch (Exception e) {
            e.printStackTrace();
            return null;
        }
    }
    /**
     * 用于释放资源
     * @param conn  连接对象
     * @param state 执行环境
     * @param result 结果集
     */
    public static void close(Connection conn , Statement state ,ResultSet result) {
        if(result!=null) {
            try {
                result.close();
            } catch (SQLException e) {
                e.printStackTrace();
            }
        }
        if(state!=null) {
            try {
                state.close();
            } catch (SQLException e) {
                // TODO Auto-generated catch block
                e.printStackTrace();
            }
        }
        if(conn!=null) {
            try {
                conn.close();
            } catch (SQLException e) {
                // TODO Auto-generated catch block
                e.printStackTrace();
            }
        }
    }

}
</code></pre>

<h3>数据库优化 *</h3>
<pre><code>1.  在进行表格查询时 , where子句中的条件执行顺序是从左至右 , 清除数据量较大的条件应该放在左边.(特别注意: 笛卡尔积消除条件必须放在最左边)

2.  在进行表格查询时 , 列名列表应避免使用*号 ! 数据库在执行查询操作时, 会先将*号展开, 转换为所有的列名, 再进行查询.

3.  在进行表格查询时 , 能使用where条件筛选的数据, 应尽量避免使用having子句来筛选. 因为where条件执行在having之前 , 在早期筛选掉大量数据, 可以让程序执行的更顺畅.

4.  在进行多表查询时 , 查询的表顺序是从右至左的. 应把表中数据量最少的表放在查询的最右边.

5.  在进行多表查询时 , 应尽可能的给所有的表添加别名, 能明确的区分有冲突的列.

6.  在使用事务时 ,  应尽量多的commit , 尽量早的commit ! 原因是: 事务在未提交时, 数据库会耗费大量的内存 , 来缓存未提交的SQL结果 !

7.  尽可能多的使用函数 来提高SQL执行的效率. 

8.  SQL语句编写时, 除字符串以外 , 应使用大写字母 ! 因为SQL语句执行时, 会先将小写字母 转换为 大写字母, 再执行.

9.  应尽可能少的访问数据库 (多次数据访问的结果可能相同, 如果缓存起来 ,可以提高程序的执行效率)

10. 在索引列上 , 尽可能避免使用not来判断. not关键字如果判断了索引列 , 会导致此次查询索引失效 , 转而使用全表扫描的方式查询.

11. 在索引列上, 不能使用算数运算 , 算数运算也会导致索引列使用, 使用全表扫描的方式进行查询.

12. 在查询数据时, 如果需要使用&gt;或&lt;的条件, 应替换为&gt;= 或 &lt;= ! 
        原因是&gt;和&lt;符号 , 查询时, 是按照&gt;= 和 &lt;= 进行查询, 然后在撇去=的结果.
</code></pre>


</body>
