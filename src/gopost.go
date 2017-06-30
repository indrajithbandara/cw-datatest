package main
import(
         "fmt"
         "net/http"
         "net/url"
         "io/ioutil"
 )
 
func main(){
        get()
        post()
}
 func get(){
         response,_:=http.Get("http://127.0.0.1/")
         defer response.Body.Close()
         body,_:=ioutil.ReadAll(response.Body)
         fmt.Println(string(body))
               
         if response.StatusCode == 200 {=
                 fmt.Println("ok")
         }else{
                 fmt.Println("error")
         }
 }
 func post(){
         //resp, err :=
         http.PostForm("http://127.0.0.1",
                 url.Values{"name": {"ruifengyun"}, "blog": {"xiaorui.cc"},
                 "aihao":{"python golang"},"content":{"nima,fuck "}})
 }