---
title: 'jFinal配置自动生成'
cover: "/img/lynk/68.jpg"
date:       2021-04-10
tags:
	- Java
	- jFinal
	
---
  
  

  
### Jfinal配置自动生成model
  
```java
package com.demo.common.model;

import javax.sql.DataSource;

import com.jfinal.kit.PathKit;
import com.jfinal.plugin.activerecord.dialect.PostgreSqlDialect;
import com.jfinal.plugin.activerecord.generator.Generator;
import com.jfinal.plugin.druid.DruidPlugin;

/**
 * 本 demo 仅表达最为粗浅的 jfinal 用法，更为有价值的实用的企业级用法 详见 JFinal 俱乐部:
 * http://jfinal.com/club
 * 
 * 在数据库表有任何变动时，运行一下 main 方法，极速响应变化进行代码重构
 */
public class _JFinalDemoGenerator {

    public static DataSource getDataSource() {
        DruidPlugin druidPlugin = new DruidPlugin(
                "jdbc:postgresql://localhost:5444/console1?currentSchema=console1", "username", "password");
        druidPlugin.start();
        return druidPlugin.getDataSource();
    }

    public static void main(String[] args) {
        // base model 所使用的包名
        String baseModelPackageName = "com.model.base";
        // base model 文件保存路径
        String baseModelOutputDir = PathKit.getWebRootPath()
                + "/src/main/java/com/model/base";

        // model 所使用的包名 (MappingKit 默认使用的包名)
        String modelPackageName = "com.model";
        // model 文件保存路径 (MappingKit 与 DataDictionary 文件默认保存路径)
        String modelOutputDir = baseModelOutputDir + "/..";

        // 创建生成器
        Generator generator = new Generator(getDataSource(), baseModelPackageName, baseModelOutputDir, modelPackageName,
                modelOutputDir);

        // 配置是否生成备注
        generator.setGenerateRemarks(true);

        // 设置数据库方言
        generator.setDialect(new PostgreSqlDialect());

        // 设置是否生成链式 setter 方法
        generator.setGenerateChainSetter(false);

        // 添加不需要生成的表名
        generator.addExcludedTable("adv");

        // 设置是否在 Model 中生成 dao 对象
        generator.setGenerateDaoInModel(false);

        // 设置是否生成字典文件
        generator.setGenerateDataDictionary(false);

        // 设置需要被移除的表名前缀用于生成modelName。例如表名 "osc_user"，移除前缀 "osc_"后生成的model名为
        // "User"而非 OscUser
        generator.setMetaBuilder(new SelfMetaBuilder(getDataSource()));

        generator.setGenerateChainSetter(true);
        // 生成
        generator.generate();
    }
}

```



```java

package com.demo.common.model;

import java.sql.ResultSet;
import java.sql.SQLException;
import java.util.List;

import javax.sql.DataSource;

import com.jfinal.plugin.activerecord.generator.MetaBuilder;
import com.jfinal.plugin.activerecord.generator.TableMeta;




public class SelfMetaBuilder extends MetaBuilder {

    /**
     * Creates a new instance of SelfMetaBuilder.<br/>
     * Description: TODO<br/>
     * 
     * @param dataSource
     */

    public SelfMetaBuilder(DataSource dataSource) {
        super(dataSource);
        // TODO Auto-generated constructor stub
    }

    @Override
    protected void buildTableNames(List<TableMeta> ret) throws SQLException {
        ResultSet rs = getTablesResultSet();
        while (rs.next()) {
            String tableName = rs.getString("TABLE_NAME");

            if (!tableName.startsWith("blog_")) {
                System.out.println("Skip table :" + tableName);
                continue;
            }
            if (isSkipTable(tableName)) {
                System.out.println("Skip table :" + tableName);
                continue;
            }

            // jfinal 4.3 新增过滤 table 机制
            if (filterPredicate != null && filterPredicate.test(tableName)) {
                System.out.println("Skip table :" + tableName);
                continue;
            }

            TableMeta tableMeta = new TableMeta();
            tableMeta.name = tableName;
            tableMeta.remarks = rs.getString("REMARKS");

            tableMeta.modelName = buildModelName(tableName);
            tableMeta.baseModelName = buildBaseModelName(tableMeta.modelName);
            ret.add(tableMeta);
        }
        rs.close();
    }

}
```

### Jfinal 初始化

```java
public class DemoConfig extends JFinalConfig {
  public void configPlugin(Plugins me) {
  DruidPlugin dp = new DruidPlugin("jdbc:mysql://localhost/db_name", "userName", "password");
    me.add(dp);
    ActiveRecordPlugin arp = new ActiveRecordPlugin(dp);
    me.add(arp);
    arp.addMapping("user", User.class);
    arp.addMapping("article", "article_id", Article.class);
  }
}
```


更多: [官方文档5.2 ActiveRecordPlugin](https://jfinal.com/doc/5-2)

