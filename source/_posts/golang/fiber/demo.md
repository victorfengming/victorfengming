---
title: "Golang Fiber 案例"
cover: "/img/lynk/62.jpg"
date:       2021-05-22
subtitle: "An Express inspired web framework"
tags:
    - Golang
    - Web
    - Fiber
---



文档地址: https://docs.gofiber.io/


# helloworld

```go
package main

import "github.com/gofiber/fiber/v2"

func main() {
	app := fiber.New()

	app.Get("/", func(c *fiber.Ctx) error {
		return c.SendString("Hello, World!")
	})

	app.Listen(":3000")
}
```






# data handled ok

```go
package main

import (
	"github.com/gofiber/fiber/v2"
	"log"
)

func main() {
	app := fiber.New()
	type Person struct {
		Name string `json:"name" xml:"name" form:"name"`
		Pass string `json:"pass" xml:"pass" form:"pass"`
	}

	type SomeStruct struct {
		rName string
		rPass string
	}

	app.Post("/api/item", func(c *fiber.Ctx) error {
		p := new(Person)

		if err := c.BodyParser(p); err != nil {
			return err
		}

		log.Println(p.Name) // john
		log.Println(p.Pass) // doe

		//return c.SendString("ok")
		return c.JSON(fiber.Map{
			"name": p.Name + ">>>handled",
			"pass": p.Pass + ">>>handled",
		})
		/**
		2021/05/22 17:43:10 victor
		2021/05/22 17:43:10 1235f

		*/
	})

	app.Get("/api/json", func(c *fiber.Ctx) error {
		// Create data struct:
		//toReturnData := SomeStruct{
		//	rName: "Grame",
		//	rPass: "20",
		//}
		//return c.SendString(c.JSON(toReturnData))
		// => Content-Type: application/json
		// => "{"Name": "Grame", "Age": 20}"

		return c.JSON(fiber.Map{
			"name": "Grame",
			"age":  20,
		})
		// => Content-Type: application/json
		// => "{"name": "Grame", "age": 20}"
	})

	app.Listen(":3000")
}

```


request

```http
POST http://localhost:3000/api/item
Content-Type: application/x-www-form-urlencoded

name=victor&pass=1235f


### HTTP/1.1 200 OK
#Date: Sat, 22 May 2021 09:59:59 GMT
#Content-Type: application/json
#Content-Length: 82
#
#{
#  "name": "victor>>>handled",
#  "pass": "1235f>>>handled"
#}
#
#Response code: 200 (OK); Time: 56ms; Content length: 52 bytes


###
GET http://localhost:3000/api/json
Accept: application/json

###


```

# select by id


```go
package main

import (
	"fmt"
	_ "github.com/go-sql-driver/mysql"
	"github.com/gofiber/fiber/v2"
	"github.com/jmoiron/sqlx"
	"log"
)

func main() {
	app := fiber.New()
	type Person struct {
		Name string `json:"name" xml:"name" form:"name"`
		Pass string `json:"pass" xml:"pass" form:"pass"`
		Id   int    `json:"id" xml:"id" form:"id"`
	}

	type SomeStruct struct {
		rName string
		rPass string
	}

	app.Post("/api/user/selectById", func(c *fiber.Ctx) error {
		p := new(Person)

		if err := c.BodyParser(p); err != nil {
			return err
		}

		log.Println(p.Id) // john
		//log.Println(p.Pass) // doe
		u := mapper(p.Id)
		//return c.SendString("ok")
		return c.JSON(fiber.Map{
			"id":   u.Id,
			"name": u.Name,
			"age":  u.Age,
		})
		/**
		2021/05/22 17:43:10 victor
		2021/05/22 17:43:10 1235f
		*/
	})

	app.Get("/api/json", func(c *fiber.Ctx) error {
		// Create data struct:
		//toReturnData := SomeStruct{
		//	rName: "Grame",
		//	rPass: "20",
		//}
		//return c.SendString(c.JSON(toReturnData))
		// => Content-Type: application/json
		// => "{"Name": "Grame", "Age": 20}"

		return c.JSON(fiber.Map{
			"name": "Grame",
			"age":  20,
		})
		// => Content-Type: application/json
		// => "{"name": "Grame", "age": 20}"
	})

	app.Listen(":3000")
	//app.Listen("192.168.1.107:3000")
}

type user struct {
	Id   int    `db:"id"`
	Age  int    `db:"age"`
	Name string `db:"name"`
}

func mapper(id int) user {
	var u user

	//
	dsn := "mp:mp@tcp(39.106.139.40:3306)/mp"
	db, err := sqlx.Open("mysql", dsn)
	if err != nil {
		fmt.Printf("connect server failed, err:%v\n", err)
		return u
	}
	db.SetMaxOpenConns(200)
	db.SetMaxIdleConns(10)

	sqlStr := "SELECT id, name, age FROM user WHERE id = ?"

	if err := db.Get(&u, sqlStr, id); err != nil {
		fmt.Printf("get data failed, err:%v\n", err)
		return u
	}
	//fmt.Printf("id:%d, name:%s, age:%d\n", u.Id, u.Name, u.Age)
	return u
}
```

request 

```http
POST http://localhost:3000/api/user/selectById
Content-Type: application/json
Accept: */*


{
  "id": 2
}




### HTTP/1.1 200 OK
#Date: Sat, 22 May 2021 09:59:59 GMT
#Content-Type: application/json
#Content-Length: 82
#
#{
#  "name": "victor>>>handled",
#  "pass": "1235f>>>handled"
#}
#
#Response code: 200 (OK); Time: 56ms; Content length: 52 bytes


###
GET http://localhost:3000/api/json
Accept: application/json

###


```


# 语音


```go
package main

import (
	"fmt"
	_ "github.com/go-sql-driver/mysql"
	"github.com/gofiber/fiber/v2"
	"github.com/jmoiron/sqlx"
	"log"
)

func main() {
	app := fiber.New()
	type Person struct {
		Name string `json:"name" xml:"name" form:"name"`
		Pass string `json:"pass" xml:"pass" form:"pass"`
		Id   int    `json:"id" xml:"id" form:"id"`
	}

	type SomeStruct struct {
		rName string
		rPass string
	}

	app.Post("/api/user/selectById", func(c *fiber.Ctx) error {
		p := new(Person)

		if err := c.BodyParser(p); err != nil {
			return err
		}

		log.Println(p.Id) // john
		//log.Println(p.Pass) // doe
		u := mapper(p.Id)
		//return c.SendString("ok")
		return c.JSON(fiber.Map{
			"id":   u.Id,
			"name": u.Name,
			"age":  u.Age,
		})
		/**
		2021/05/22 17:43:10 victor
		2021/05/22 17:43:10 1235f
		*/
	})

	app.Get("/api/json", func(c *fiber.Ctx) error {
		// Create data struct:
		//toReturnData := SomeStruct{
		//	rName: "Grame",
		//	rPass: "20",
		//}
		//return c.SendString(c.JSON(toReturnData))
		// => Content-Type: application/json
		// => "{"Name": "Grame", "Age": 20}"

		return c.JSON(fiber.Map{
			"name": "Grame",
			"age":  20,
		})
		// => Content-Type: application/json
		// => "{"name": "Grame", "age": 20}"
	})

	app.Listen(":3000")
	//app.Listen("192.168.1.107:3000")
}

type user struct {
	Id   int    `db:"id"`
	Age  int    `db:"age"`
	Name string `db:"name"`
}

func mapper(id int) user {

	var u user

	dsn := "mp:mp@tcp(39.106.139.40:3306)/mp"
	db, err := sqlx.Open("mysql", dsn)
	if err != nil {
		fmt.Printf("connect server failed, err:%v\n", err)
		return u
	}
	db.SetMaxOpenConns(200)
	db.SetMaxIdleConns(10)

	sqlStr := "SELECT id, name, age FROM user WHERE id = ?"

	if err := db.Get(&u, sqlStr, id); err != nil {
		fmt.Printf("get data failed, err:%v\n", err)
		return u
	}
	//fmt.Printf("id:%d, name:%s, age:%d\n", u.Id, u.Name, u.Age)
	return u
}

```


# 讯飞语音

```go
package main

import (
	"crypto/hmac"
	"crypto/sha256"
	"encoding/base64"
	"encoding/json"
	"fmt"
	"io/ioutil"
	"net/http"
	"net/url"
	"os"
	"strings"
	"time"
	"github.com/gorilla/websocket"
)

/**
 * 语音听写流式 WebAPI 接口调用示例 接口文档（必看）：https://doc.xfyun.cn/rest_api/语音听写（流式版）.html
 * webapi 听写服务参考帖子（必看）：http://bbs.xfyun.cn/forum.php?mod=viewthread&tid=38947&extra=
 * 语音听写流式WebAPI 服务，热词使用方式：登陆开放平台https://www.xfyun.cn/后，找到控制台--我的应用---语音听写---服务管理--上传热词
 * 注意：热词只能在识别的时候会增加热词的识别权重，需要注意的是增加相应词条的识别率，但并不是绝对的，具体效果以您测试为准。
 * 错误码链接：https://www.xfyun.cn/document/error-code （code返回错误码时必看）
 * @author iflytek
 * 选择采样率: 16000
 * pcm >>> mp3 : http://www.freestudytool.com/item/pcm_to_mp3


 * 体验特色发音: https://www.xfyun.cn/services/online_tts
各位旅客请注意，飞往无锡的ZH9556次航班已经开始登机，请携带好随身物品到31号登机口上飞机，祝您旅途愉快，谢谢！Dear passengers, please note that the zh9556flight to Wuxi is already on board. Please bring your belongings to board 31and have a pleasant journey. Thank you!

 */
var (
	hostUrl   = "wss://tts-api.xfyun.cn/v2/tts"
	apiKey    = "3931dc0b958776b5464d269fd20407b8"
	apiSecret = "MDA1OTY1Y2Q2ODAyNTQ0ODFiYjVkMmY1"
	file      = "test.pcm" //请填写您的音频文件路径
	appid     = "f6d3c990"
)

const (
	STATUS_FIRST_FRAME    = 0
	STATUS_CONTINUE_FRAME = 1
	STATUS_LAST_FRAME     = 2
)

func main() {
	fmt.Println(HmacWithShaTobase64("hmac-sha256", "hello\nhello", "hello"))
	st := time.Now()
	d := websocket.Dialer{
		HandshakeTimeout: 5 * time.Second,
	}

	var srcText string = "各位旅客请注意，飞往伊春的ZH9556次航班已经开始登机，请携带好随身物品到31号登机口上飞机，祝您旅途愉快，谢谢！"

	//握手并建立websocket 连接
	conn, resp, err := d.Dial(assembleAuthUrl(hostUrl, apiKey, apiSecret), nil)
	if err != nil {
		panic(readResp(resp) + err.Error())
		return
	} else if resp.StatusCode != 101 {
		panic(readResp(resp) + err.Error())
	}

	defer conn.Close()

	frameData := map[string]interface{}{
		"common": map[string]interface{}{
			"app_id": appid, //appid 必须带上，只需第一帧发送
		},
		"business": map[string]interface{}{ //business 参数，只需一帧发送
			"vcn":   "xiaoyan",
			"aue":   "raw",
			"speed": 50,
			"tte":   "UTF8",
		},
		"data": map[string]interface{}{
			"status":   STATUS_LAST_FRAME,
			"encoding": "UTF8",
			"text":     base64.StdEncoding.EncodeToString([]byte(srcText)),
		},
	}
	fmt.Println("send first")
	conn.WriteJSON(frameData)

	//获取返回的数据
	//var decoder Decoder
	audioFile, err := os.OpenFile(file, os.O_RDWR|os.O_CREATE|os.O_TRUNC, os.ModePerm)
	if err != nil {
		panic(err)
	}
	for {
		var resp = RespData{}
		_, msg, err := conn.ReadMessage()
		if err != nil {
			fmt.Println("read message error:", err)
			break
		}
		json.Unmarshal(msg, &resp)
		//fmt.Println(string(msg))
		//fmt.Println(resp.Data.Audio, resp.Sid)
		if resp.Code != 0 {
			fmt.Println(resp.Code, resp.Message, time.Since(st))
			return
		}
		//decoder.Decode(&resp.Data.Audio)

		audiobytes, err := base64.StdEncoding.DecodeString(resp.Data.Audio)
		if err != nil {
			panic(err)
		}
		_, err = audioFile.Write(audiobytes)
		if err != nil {
			panic(err)
		}

		if resp.Data.Status == 2 {
			//cf()
			//fmt.Println("final:",decoder.String())

			fmt.Println(resp.Code, resp.Message, time.Since(st))
			break
			//return
		}

	}
	audioFile.Close()

	time.Sleep(1 * time.Second)
}

type RespData struct {
	Sid     string `json:"sid"`
	Code    int    `json:"code"`
	Message string `json:"message"`
	Data    Data   `json:"data"`
}

type Data struct {
	Audio  string `json:"audio,omitempty"`
	Ced    int    `json:"ced,omitempty"`
	Status int    `json:"status,omitempty"`
}

//创建鉴权url  apikey 即 hmac username
func assembleAuthUrl(hosturl string, apiKey, apiSecret string) string {
	ul, err := url.Parse(hosturl)
	if err != nil {
		fmt.Println(err)
	}
	//签名时间
	date := time.Now().UTC().Format(time.RFC1123)
	//date = "Tue, 28 May 2019 09:10:42 MST"
	//参与签名的字段 host ,date, request-line
	signString := []string{"host: " + ul.Host, "date: " + date, "GET " + ul.Path + " HTTP/1.1"}
	//拼接签名字符串
	sgin := strings.Join(signString, "\n")
	fmt.Println(sgin)
	//签名结果
	sha := HmacWithShaTobase64("hmac-sha256", sgin, apiSecret)
	fmt.Println(sha)
	//构建请求参数 此时不需要urlencoding
	authUrl := fmt.Sprintf("hmac username=\"%s\", algorithm=\"%s\", headers=\"%s\", signature=\"%s\"", apiKey,
		"hmac-sha256", "host date request-line", sha)
	//将请求参数使用base64编码
	authorization := base64.StdEncoding.EncodeToString([]byte(authUrl))

	v := url.Values{}
	v.Add("host", ul.Host)
	v.Add("date", date)
	v.Add("authorization", authorization)
	//将编码后的字符串url encode后添加到url后面
	callurl := hosturl + "?" + v.Encode()
	return callurl
}

func HmacWithShaTobase64(algorithm, data, key string) string {
	mac := hmac.New(sha256.New, []byte(key))
	mac.Write([]byte(data))
	encodeData := mac.Sum(nil)
	return base64.StdEncoding.EncodeToString(encodeData)
}

func readResp(resp *http.Response) string {
	if resp == nil {
		return ""
	}
	b, err := ioutil.ReadAll(resp.Body)
	if err != nil {
		panic(err)
	}
	return fmt.Sprintf("code=%d,body=%s", resp.StatusCode, string(b))
}

// 解析返回数据，仅供demo参考，实际场景可能与此不同。
type Decoder struct {
	results []*Result
}

func (d *Decoder) Decode(result *Result) {
	if len(d.results) <= result.Sn {
		d.results = append(d.results, make([]*Result, result.Sn-len(d.results)+1)...)
	}
	if result.Pgs == "rpl" {
		for i := result.Rg[0]; i <= result.Rg[1]; i++ {
			d.results[i] = nil
		}
	}
	d.results[result.Sn] = result
}

func (d *Decoder) String() string {
	var r string
	for _, v := range d.results {
		if v == nil {
			continue
		}
		r += v.String()
	}
	return r
}

type Result struct {
	Ls  bool   `json:"ls"`
	Rg  []int  `json:"rg"`
	Sn  int    `json:"sn"`
	Pgs string `json:"pgs"`
	Ws  []Ws   `json:"ws"`
}

func (t *Result) String() string {
	var wss string
	for _, v := range t.Ws {
		wss += v.String()
	}
	return wss
}

type Ws struct {
	Bg int  `json:"bg"`
	Cw []Cw `json:"cw"`
}

func (w *Ws) String() string {
	var wss string
	for _, v := range w.Cw {
		wss += v.W
	}
	return wss
}

type Cw struct {
	Sc int    `json:"sc"`
	W  string `json:"w"`
}

```