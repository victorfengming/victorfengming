---
title: 'JDBC笔记01'
cover: "/img/lynk/77.jpg"
date:       2019-11-08
subtitle: 'JDBC,Connection,Statement,ResultSet,PreparedStatement,Properties' 
tags:
	- Java
	- basis
	- JDBC
---

  
  
* content  
{:toc}  
  
  
  
  


### 学习目标  
- [ ] 理解`JDBC`原理
- [ ] 掌握`Connection`接口的使用
- [ ] 掌握`Statement`接口的使用
- [ ] 掌握`ResultSet`接口的使用
- [ ] 掌握`PreparedStatement`接口的使用
- [ ] 掌握`Properties`类与配置文件的使用



### JDBC 概念
JDBC  (`Java DataBase Connectivity`)
Java数据库连接技术的简称，提供连接各种常用数据库的能力
说白了就是java语言连接数据库
```
有一个程序员,他要写一套程序,但是他不知道公司用什么数据库

所以,他就得学java连mysql连Oracle,连DB2,
市面上所有的关系型数据库,他都得学习一遍,对吧!

而我们期望使用统一的一套Java代码可以操作所有的关系型数据库
有一个程序员终于忍不住了,写了个JDBC
JDBC:定义了操作所有关系型数据库的规则(接口)

这里只是写了接口,但是没有写具体的实现类,那么这个实现类谁写呢

sun公司说了,每一个数据库的厂商你们自己写实现类
所以每个数据库厂商都写了不同的实现类,不同版本的实现类

我们给这个实现类起了个名字,叫做数据库驱动

```

`JDBC`本质:其实就是官方(`Sun`公司)定义的一套操作所有关系型数据库的规则,及接口.
各个数据库厂商去实现这套接口,提供数据库驱动`jar`包.我们可以使用这套接口(`JDBC`)编程,真正执行的代码是驱动`jar`包中的实现类.

## `JDBC`快速入门


### 步骤:
1. 导入驱动`jar`包
    官网`mysql`驱动`jar`包下载地址:[mysql/mysql-connector-java](http://central.maven.org/maven2/mysql/mysql-connector-java/)
    1. 复制`mysql-connector-java-5.1.37.jar`
    2. 右键-->`Add as library`
    
2. 注册驱动
3. 获取数据库的连接对象
4. 定义`sql`
5. 获取执行`sql`语句的对象 `statement`
6. 执行`sql`,接收返回结果
7. 处理结果
8. 释放资源



### 实例代码
别管能不能看懂,直接我就上一堆代码,然后再解释
```java
package cn.itcast.jdbc;

import java.sql.Connection;
import java.sql.DriverManager;
import java.sql.Statement;

/**
 * @author victor
 * @site https://victorfengming.gitee.io/
 * @company XDL
 * @project itcast
 * @package cn.itcast.jdbc
 * @created 2019-11-07 23:43
 * @function ""
 */
public class JdbcDemo01 {

    public static void main(String[] args) throws Exception {
        // 1. 导入驱动jar包
        // 2.注册驱动
        Class.forName("com.mysql.jdbc.Driver");
        // 3.获取数据库连接对象
        Connection conn = DriverManager.getConnection("jdbc:mysql://localhost:3306/plan","root","");

        //4. 定义sql
        String sql = "use plan";
        //5. 获取执行sql语句的对象 statement
        Statement stmt = conn.createStatement();
        //6. 执行sql,接收返回结果
        int count = stmt.executeUpdate(sql);
        //7. 处理结果
        System.out.println(count);
        //8. 释放资源
        stmt.clearBatch();
        conn.close();
    }
}
```



### 详解各个对象




#### `DriverManager` ：  
驱动管理对象,用于管理`JDBC`驱动, 功能如下:




##### 1. 注册驱动  
1. 注册与给定的驱动程序`static void registerDriver(Driver driver)`  
2. 写代码使用:  
    1. `Class.forName("com.mysql.jdbc.Driver");`好像这个类中有一个静态代码块,这里面有现成的代码
    2. 通过查看源码发现:在`com.mysql.jdbc.Driver`类中存在静态代码块
    ```java
   static {
            try {
                DriverManager.registerDriver(new Driver());
            } catch (SQLException var1) {
                throw new RuntimeException("Can't register driver!");
            }
        }
    ```
3. 补充:
    - 在`mysql-connector-java-5.1.37.jar` 的`5`版本之后 
    - 有一个文件在`mysql-connector-java-5.1.37.jar/META-INF/services/java.sql.Driver`里面
    - 这个文件可以让你省略注册驱动的步骤,好吧!




##### 2. 获取数据库连接:

方法:`static Connection getConnection(String url,String user,String password)`

参数:
    - `url`:指定连接的路径
        - 语法:`jdbc:mysql://ip地址(域名):端口号/数据库名称`
        - 例子:`jdbc:mysql://localhost:3306/plan`
        - 细节:如果连接的是本机的`mysql`服务器,并且mysql服务器默认端口是3306,则url可以简写为`:jdbc:mysql///数据库名称`
        - 例如:`Connection conn = DriverManager.getConnection("jdbc:mysql:///plan","root","");`
    - `user`:用户名
    - `password`:密码
    
    




#### `Connection` ：数据库连接对象,用于连接数据库并传送数据 




##### 1. 获取执行`sql`的对象
- `Statement createStatement`
- `PreparedStatement prepareStatement(String sql)`




##### 2. 管理事务:
- 开启事务: `setAutoCommit(boolean autoCommit)`: 调用改方法设置参数为`false`,就开启事务啦,哈哈
- 提交事务: `commit()`
- 回滚事务: `rollback()`    




#### `Statement` ：执行`sql`的对象,负责执行`SQL`语句




##### 执行`sql`
- `boolean execute(String sql)` :可以执行任意的`sql`,可能会返回多个结果!(了解即可)
- `int executeUpdate(String sql)`:        
    - 执行`DML(insert,update,delete)`语句,`DDL(create,alter,drop)`语句
    - 这个`DDL`不经常用,所有在这个地方我们都是用前者的
    - 返回值: 执行语句后,所影响的行数,我们可以通过这个影响的行数判断DML语句是否执行成功,要是大于0就成功了呗,反之,则失败.
- `ResultSet executeQuery(String sql)`: 执行`DQL(select)`语句




##### 练习:见附录
     

#### `ResultSet`：结果集对象,负责保存Statement执行后所产生的查询结果




##### `next()`:
- 游标向下移动一行
- 并且判断当前行是否是最后一行的末尾
- 返回`boolean`,如果有数据返回true,反之亦然!




##### `getXxx(参数)`:获取数据
- Xxx:代表数据类型 如:`int getInt(), String getString()`
- 参数:
    - `int`: 代表列的编号, 从1开始 如`getString(1)`
    - `String`: 代表列名称. 如: `getDouble("balance")`




##### - 注意:
使用步骤:
1. 游标向下移动一行
2. 判断是否有数据
3. 获取数据




##### - 练习:
定义一个方法,查询emp表的数据将其封装为对象,然后装载集合,返回.
- 定义`Emp`类 用于封装`Emp`表数据的`JavaBean`
- 定义方法 `public List<Emp> findAll(){}`
- 实现方法 `select * from emp;`




#### `PreparedStatement` : 执行`sql`的对象,用于负责执行`SQL`语句




##### 1. SQL注入问题:在拼接sql时,有一些特殊关键字参与字符串的拼接.会造成安全性的问题.
1. 输入用户名随便,输入密码:`a' or 'a' = 'a`
2. sql:`select * from user where username = 'victor' and password = 'a' or 'a' = 'a'`




##### 2. 解决sql注入问题:使用PreparedStatement对象来解决,他是




##### 3. 预编译sql:参数使用?作为占位符




##### 4. 使用步骤:


1. 导入驱动包


2. 注册驱动


3. 获取数据库对象连接


4. 定义sql
- 注意:sql的参数使用?作为占位符.如:`select * from user where username = ? and password = ?;`


5. 获取执行sql语句的对象PreparedStatement Connection.prepareStatement(String sql)


6. 给? 赋值:
- 方法: setXxx(参数1,参数2)
    - 参数1:?的位置编号 从1 开始
    - 参数2:?的值


6. 执行sql,接受返回结果,不需要传递sql语句


7. 处理结果


8. 释放资源





##### 5. 注意:后期都会使用PreparedStatement来完成增删改查的所有操作
1. 可以防止SQL注入
2. 效率更高





### 抽取JDBC工具类 : `JdbcUtils.java`




#### - 目的 : 简化书写




#### - 分析 : 




##### 1. 注册驱动




##### 2. 抽取一个方法获取连接对象
需求 : 不想传递参数(麻烦),还得保证工具类的通用性.
解决 : 配置文件    jdbc.properties
```java
url=jdbc:mysql:///plan
user=root
password=
driver=com.mysql.jdbc.Driver
```




#### - 练习:




##### - 需求 : 
- 通过键盘录入用户名和密码
- 判断用户是否登录成功
    - `select * from user where username = "and password = ""`
    - 如果这个sql有结果,则查询成功,反之失败




##### - 步骤 :
创建数据库表  user
```sql
create table user(
    id int primary key auto_increment,
    username varchar(32),
    password varchar(32)
);
```
插入数据
```sql
insert into user
values (null,"victor","123");

insert into user
values (null,"ttkr","1907123");
```


### JDBC控制事务:




#### 1. 事务: 一个包含多个步骤的业务操作.如果这个业务操作被事务管理,则这多个步骤要么同事成功,要么同时失败.




#### 2. 操作:
- 开始事务
- 提交事务
- 回滚事务





#### 3. 使用Connection对象来管理事务
- 开启事务:setAutoCommit(boolean autoCommit) :调用改方法设置参数为false,即开启事务
- 提交事务: commit()
- 回滚事务: rollback()
    - catch中回滚事务
    
    
# 附录(源代码)
   


### `account`表 添加一条记录  

```java
package cn.itcast.jdbc;

import java.sql.Connection;
import java.sql.DriverManager;
import java.sql.SQLException;
import java.sql.Statement;

/**
 * @author victor
 * @site https://victorfengming.gitee.io/
 * @company XDL
 * @project itcast
 * @package cn.itcast.jdbc
 * @created 2019-11-08 14:41
 * @function "用于插入数据"
 */
public class JdbcDemo02 {
    public static void main(String[] args) {
        Statement stmt = null;

        try {
            // 1.注册驱动
            // 这行不写也行
            //  Class.forName("com.mysql.jdbc.Driver");
            // 2. 定义sql
            //  String sql = "insert into account values(null,'ttk',6299)";
            String sql = "insert into account values(null,'yupeng',5666)";
            // 获取Connection对象

            Connection conn = DriverManager.getConnection("jdbc:mysql:///plan", "root", "");
            // 4获取执行sql对象 Statement
            stmt = conn.createStatement();
            // 5 执行sql
            int count = stmt.executeUpdate(sql);
            // count影响的行数
            // 6.处理结果
            System.out.println(count);
            if (count > 0) {
                System.out.println("提交成功");

            } else {
                System.out.println("添加失败");
            }

        } catch (Exception e) {
            e.printStackTrace();
        } finally {
            // 释放资源
            // 为了避免空指针异常需要判断
            if (stmt != null) {
                try {
                    stmt.close();
                } catch (SQLException e) {
                    e.printStackTrace();
                }
            }
        }
    }
}

```




### `account`表 删除一条记录  


```java
package cn.itcast.jdbc;

import java.sql.Connection;
import java.sql.DriverManager;
import java.sql.SQLException;
import java.sql.Statement;

/**
 * @author victor
 * @site https://victorfengming.gitee.io/
 * @company XDL
 * @project itcast
 * @package cn.itcast.jdbc
 * @created 2019-11-08 15:35
 * @function "从表中删除记录"
 */
public class JdbcDemo04 {
    public static void main(String[] args) {
        Connection conn = null;
        Statement stmt = null;
        try {
            // 1.注册表
            // 2.获取连接对象
            conn = DriverManager.getConnection("jdbc:mysql:///plan","root","");
            // 3. 定义sql
            String sql = "delete from account where id = 4";
            // 4.获取执行sql对象
            stmt = conn.createStatement();
            // 5.执行sql
            int count = stmt.executeUpdate(sql);
            // 6.处理结果
            if (count > 0) {
                System.out.println("运行成功");
            } else {
                System.out.println("失败了!");
            }

        } catch (Exception e) {
            e.printStackTrace();
        }finally {
            // 7. 释放资源
            if (stmt != null) {
                try {
                    stmt.close();
                } catch (SQLException e) {
                    e.printStackTrace();
                }
            }
        }
    }

}

```
 
        


### `account`表 修改一条记录  


```java
package cn.itcast.jdbc;

import java.sql.Connection;
import java.sql.DriverManager;
import java.sql.SQLException;
import java.sql.Statement;

/**
 * @author victor
 * @site https://victorfengming.gitee.io/
 * @company XDL
 * @project itcast
 * @package cn.itcast.jdbc
 * @created 2019-11-08 15:16
 * @function "account表修改记录"
 */
public class JdbcDemo03 {
    public static void main(String[] args) {
        Connection conn = null;
        Statement stmt = null;
        try {
            // 1.注册表
            // 2.获取连接对象
            conn = DriverManager.getConnection("jdbc:mysql:///plan","root","");
            // 3. 定义sql
            String sql = "update account set balance = 6060 where id = 2";
            // 4.获取执行sql对象
            stmt = conn.createStatement();
            // 5.执行sql
            int count = stmt.executeUpdate(sql);
            // 6.处理结果
            if (count > 0) {
                System.out.println("运行成功");
            } else {
                System.out.println("失败了!");
            }

        } catch (Exception e) {
            e.printStackTrace();
        }finally {
            // 7. 释放资源
            if (stmt != null) {
                try {
                    stmt.close();
                } catch (SQLException e) {
                    e.printStackTrace();
                }
            }
        }
    }
}
```




### `DDl`: 创建一个表  


```java
package cn.itcast.jdbc;

import java.sql.Connection;
import java.sql.DriverManager;
import java.sql.SQLException;
import java.sql.Statement;

/**
 * @author victor
 * @site https://victorfengming.gitee.io/
 * @company XDL
 * @project itcast
 * @package cn.itcast.jdbc
 * @created 2019-11-08 15:40
 * @function "用于创建一个新表"
 */
public class JdbcDemo05 {
    public static void main(String[] args) {
        Connection conn = null;
        Statement stmt = null;
        try {
            // 1.注册表
            // 2.获取连接对象
            conn = DriverManager.getConnection("jdbc:mysql:///plan","root","");
            // 3. 定义sql
            String sql = "create table student (id int ,name varchar(20))";
            // 4.获取执行sql对象
            stmt = conn.createStatement();
            // 5.执行sql
            int count = stmt.executeUpdate(sql);
            // 6.处理结果
            if (count > 0) {
                System.out.println("运行成功");
            } else {
                System.out.println("失败了!");
            }

        } catch (Exception e) {
            e.printStackTrace();
        }finally {
            // 7. 释放资源
            if (stmt != null) {
                try {
                    stmt.close();
                } catch (SQLException e) {
                    e.printStackTrace();
                }
            }
        }
    }
}
```




### `account`表 查询一条记录  


```java
package cn.itcast.jdbc;

import java.sql.*;

/**
 * @author victor
 * @site https://victorfengming.gitee.io/
 * @company XDL
 * @project itcast
 * @package cn.itcast.jdbc
 * @created 2019-11-08 16:01
 * @function "查询是重中之重"
 */
public class JdbcDemo06 {
    public static void main(String[] args) {
        Connection conn = null;
        Statement stmt = null;
        ResultSet rs = null;
        try {
            // 1.注册表
            // 2.获取连接对象
            conn = DriverManager.getConnection("jdbc:mysql:///plan", "root", "");
            // 3. 定义sql
            String sql = "select * from account";
            // 4.获取执行sql对象
            stmt = conn.createStatement();
            // 5.执行sql
            rs = stmt.executeQuery(sql);
            // 6.处理结果
            // 6.1 让游标向下移动一行
            // 循环判断游标是否最后一行末尾
            while (rs.next()) {
                //            获取数据
                int id = rs.getInt(1);
                String name = rs.getString("name");
                double balance = rs.getDouble(3);
                System.out.println(id + "---" + name + "---" + balance);

            }

        } catch (Exception e) {
            e.printStackTrace();
        } finally {
            // 7. 释放资源
            if (stmt != null) {
                try {
                    stmt.close();
                } catch (SQLException e) {
                    e.printStackTrace();
                }
            }
        }
    }
}
```



### 工具类
```java
package cn.itcast.util;

import java.io.FileReader;
import java.io.IOException;
import java.net.URL;
import java.sql.*;
import java.util.Properties;

/**
 * @author victor
 * @site https://victorfengming.gitee.io/
 * @company XDL
 * @project itcast
 * @package cn.itcast.util
 * @created 2019-11-09 10:40
 * @function "JDBC工具类"
 */
public class JdbcUtils {

    //声明三个成员变量
    // 因为只有静态变量才能被静态代码块所访问,被静态方法所访问
    private static String url;
    private static String user;
    private static String password;
    private static String driver;

    /**
     * 文件的读取,只需要读取一次即可拿到这些值
     * 我们可以使用静态代码块
     * 因为静态代码块是随着类加载进行加载的
     * 只读取一次
     */

    static {
        // 读取资源文件,获取值
        try {
            // 1. 创建 Properties集合类
            Properties pro = new Properties();
            // 2.加载文件
//            pro.load(new FileReader("D:\\IdeaProjects\\itcast\\day04-JDBC\\src\\jdbc.properties"));
            // 这么写指定不行
            // 获取src路径下的文件的方式-->ClassLoader 类加载器
            ClassLoader classLoader = JdbcUtils.class.getClassLoader();
            // 这里的相对路径就是src
            URL res = classLoader.getResource("jdbc.properties");
            // 这里URL表示统一资源对应符
            String path = res.getPath();
//            System.out.println(path);
            pro.load(new FileReader(path));
            // 3.获取属性,赋值
            url = pro.getProperty("url");
            user = pro.getProperty("user");
            password = pro.getProperty("password");
            driver = pro.getProperty("driver");
            // 4. 注册驱动
            Class.forName(driver);
        } catch (IOException e) {
            e.printStackTrace();
        } catch (ClassNotFoundException e) {
            e.printStackTrace();
        }
    }


    /**
     * 获取连接
     * @return 连接对象
     */
//    public static Connection getConnection(String url,String user,String password,String driver) throws SQLException {
//        return DriverManager.getConnection(url, user, password);
//    }
//    这个地方,我既不想用传递参数的方式,还想要简化书写,这可咋整,我们这里使用配置文件的方式,所以要这样写
    public static Connection getConnection() throws SQLException {
        return DriverManager.getConnection(url, user, password);
    }

    /**
     * 释放资源方法
     */
    public static void close(Statement stmt, Connection conn) {
        if (stmt != null) {
            try {
                stmt.close();
            } catch (SQLException e) {
                e.printStackTrace();
            }
        }
        if (conn != null) {
            try {
                conn.close();
            } catch (SQLException e) {
                e.printStackTrace();
            }
        }
    }

    /**
     * 释放资源方法重载
     */
    public static void close(ResultSet rs, Statement stmt, Connection conn) {
        if (rs != null) {
            try {
                rs.close();
            } catch (SQLException e) {
                e.printStackTrace();
            }
        }
        if (stmt != null) {
            try {
                stmt.close();
            } catch (SQLException e) {
                e.printStackTrace();
            }
        }
        if (conn != null) {
            try {
                conn.close();
            } catch (SQLException e) {
                e.printStackTrace();
            }
        }
    }
}

```




### 查询emp表的数据将其封装为对象
```java
package cn.itcast.jdbc;

import cn.itcast.domain.Emp;
import cn.itcast.util.JdbcUtils;


import java.sql.*;
import java.util.ArrayList;
import java.util.Date;
import java.util.List;

/**
 * @author victor
 * @site https://victorfengming.gitee.io/
 * @company XDL
 * @project itcast
 * @package cn.itcast.jdbc
 * @created 2019-11-08 23:38
 * @function "定义一个方法,查询emp表的数据将其封装为对象,然后装载集合,返回"
 */
public class JdbcDemo08 {

    public static void main(String[] args) {
        List<Emp> list = new JdbcDemo08().findAll2();
        for (Emp emp : list) {
            System.out.println(emp);
        }
    }

    /**
     * 查询所有emp对象
     *
     * @return
     */
    public List<Emp> findAll() {
        //提前声明一些变量,以便于能够在try和catch中来回穿梭
        Connection conn = null;
        Statement stmt = null;
        ResultSet rs = null;
        List<Emp> list = null;

        try {
            // 1.注册,为了能够兼容mysql5以下的版本,所以写上
            Class.forName("com.mysql.jdbc.Driver");
            // 2.获取连接
            conn = DriverManager.getConnection("jdbc:mysql:///plan", "root", "");
            // 3.定义sql
            String sql = "select * from emp";
            // 4. 获取执行sql的对象
            stmt = conn.createStatement();
            // 5.执行sql
            rs = stmt.executeQuery(sql);
            // 先创建一个引用就ok
            Emp emp = null;
            list = new ArrayList<Emp>();
            // 6.遍历结果集
            while (rs.next()) {
                // 7.获取数据
                int id = rs.getInt("id");
                String ename = rs.getString("ename");
                int job_id = rs.getInt("job_id");
                int mgr = rs.getInt("mgr");
                // 这个sqlDate是Date 的子类,所以是可以直接进行赋值的
                Date joindate = rs.getDate("joindate");
                double bonus = rs.getDouble("bonus");
                double salary = rs.getDouble("salary");
                int dept_id = rs.getInt("dept_id");
                // 创建emp对象
                emp = new Emp();
                emp.setId(id);
                emp.setEname(ename);
                emp.setJob_id(job_id);
                emp.setMgr(mgr);
                emp.setJoindate(joindate);
                emp.setBonus(bonus);
                emp.setSalary(salary);
                emp.setDept_id(dept_id);

                // 装载集合
                list.add(emp);
            }

        } catch (Exception e) {
            e.printStackTrace();
        }finally {
            // 7. 释放资源
            if (stmt != null) {
                try {
                    stmt.close();
                } catch (SQLException e) {
                    e.printStackTrace();
                }
            }

            if (rs != null) {
                try {
                    rs.close();
                } catch (SQLException e) {
                    e.printStackTrace();
                }
            }
            if (conn != null) {
                try {
                    conn.close();
                } catch (SQLException e) {
                    e.printStackTrace();
                }
            }
        }
        return list;
    }  /**
     * 演示JDBC工具类
     *
     * @return
     */
    public List<Emp> findAll2() {
        //提前声明一些变量,以便于能够在try和catch中来回穿梭
        Connection conn = null;
        Statement stmt = null;
        ResultSet rs = null;
        List<Emp> list = null;

        try {
            // 1.注册,为了能够兼容mysql5以下的版本,所以写上
            // 2.获取连接
            conn = JdbcUtils.getConnection();
            // 3.定义sql
            String sql = "select * from emp";
            // 4. 获取执行sql的对象
            stmt = conn.createStatement();
            // 5.执行sql
            rs = stmt.executeQuery(sql);
            // 先创建一个引用就ok
            Emp emp = null;
            list = new ArrayList<Emp>();
            // 6.遍历结果集
            while (rs.next()) {
                // 7.获取数据
                int id = rs.getInt("id");
                String ename = rs.getString("ename");
                int job_id = rs.getInt("job_id");
                int mgr = rs.getInt("mgr");
                // 这个sqlDate是Date 的子类,所以是可以直接进行赋值的
                Date joindate = rs.getDate("joindate");
                double bonus = rs.getDouble("bonus");
                double salary = rs.getDouble("salary");
                int dept_id = rs.getInt("dept_id");
                // 创建emp对象
                emp = new Emp();
                emp.setId(id);
                emp.setEname(ename);
                emp.setJob_id(job_id);
                emp.setMgr(mgr);
                emp.setJoindate(joindate);
                emp.setBonus(bonus);
                emp.setSalary(salary);
                emp.setDept_id(dept_id);

                // 装载集合
                list.add(emp);
            }

        } catch (Exception e) {
            e.printStackTrace();
        }finally {
            // 7. 释放资源
            JdbcUtils.close(rs,stmt,conn);
        }
        return list;
    }
}

```



### 用户登录案例
```java
package cn.itcast.jdbc;

import cn.itcast.util.JdbcUtils;
import cn.itcast.util.python;

import java.sql.*;

/**
 * @author victor
 * @site https://victorfengming.gitee.io/
 * @company XDL
 * @project itcast
 * @package cn.itcast.jdbc
 * @created 2019-11-09 11:52
 * @function "- 需求 :
 * - 通过键盘录入用户名和密码
 * - 判断用户是否登录成功"
 */
public class JdbcDemo09 {

    public static void main(String[] args) {
        // 1.键盘录入,接收用户名和密码
        String username = python.input("请输入用户名:");
        String password = python.input("请输入密码:");
        // 2.调用用方法
        //创建对象
        boolean flag = new JdbcDemo09().login(username, password);
        // 3.判断结果,输出不同语句
        if (flag) {
            System.out.println("登录成功");
        } else {
            System.out.println("用户名或者密码错误");
        }
    }



    /**
     * 登录方法
     */
    public boolean login(String username, String password) {
        Connection conn = null;
        PreparedStatement pstmt = null;
        ResultSet rs = null;
        try {
            if (username != null || password != null) {
                ;
            }
            // 连接数据库判断是否登录成功
            // 1.获取连接
            conn = JdbcUtils.getConnection();
            // 2.定义sql
            String sql = "select * from user where username = ? and password = ?";
            System.out.println(sql);
            // 3获取执行sql的对象
            // stmt = conn.createStatement();
            // 升级版本的
            pstmt = conn.prepareStatement(sql);
            // 4执行查询
            //  rs = pstmt.executeQuery(sql);
            // 这里不需要传递参数了
            rs = pstmt.executeQuery();
            // 5判断
            // 要是查到了, 唉, 就直接就返回true
            //            if (rs.next()) {
            //                // 如果有下一行则返回true
            //                return true;
            //            } else {
            //                return false;
            //            }
            // 上面的代码就是垃圾代码
            // 如果有下一行则返回true
            return rs.next();

        } catch (SQLException e) {
            e.printStackTrace();
            //        去改配置文件, 数据库要db4
            // 这里就体现了JdbcUtils类的可扩展性很强了,不用改代码都
        }finally {
            // 释放资源
            JdbcUtils.close(rs,pstmt,conn);
        }

        return false;
    }
}

```



### 转账案例
```java
package cn.itcast.jdbc;

import cn.itcast.util.JdbcUtils;

import java.sql.Connection;
import java.sql.PreparedStatement;
import java.sql.SQLException;

/**
 * @author victor
 * @site https://victorfengming.gitee.io/
 * @company XDL
 * @project itcast
 * @package cn.itcast.jdbc
 * @created 2019-11-09 14:07
 * @function "事务操作"
 */
public class JdbcDemo10 {
    public static void main(String[] args) {
        transfer();
    }


    /**
     * 转账函数
     */
    public static void transfer() {
        Connection conn = null;
        PreparedStatement pstmt1 = null;
        PreparedStatement pstmt2 = null;
        try {
            // 1.获取来接
            conn = JdbcUtils.getConnection();
            // 2. 定义sql
            //2.1 victor+500
            String sql1 = "update account set balance = balance + ? where id = ?";
            // 2.2 ttkr -50
            String sql2 = "update account set balance = balance - ? where id = ?";
            // 3.获取执行sql对象
            pstmt1 = conn.prepareStatement(sql1);
            pstmt2 = conn.prepareStatement(sql2);
            // 设置参数
            pstmt1.setDouble(1,500);
            pstmt1.setDouble(2,1);

            pstmt2.setDouble(1,500);
            pstmt2.setDouble(2,2);

            // 5.执行sql
            pstmt1.executeUpdate();
            // 手动制造异常
            int i = 3/0;
            pstmt2.executeUpdate();

        } catch (Exception e) {
            // 事务回滚
            try {
                if (conn != null) {
                    conn.rollback();
                }
            } catch (SQLException ex) {
                ex.printStackTrace();
            }
            e.printStackTrace();
        }finally {
            JdbcUtils.close(pstmt1,conn);
            JdbcUtils.close(pstmt2,null);

        }
    }
}

```