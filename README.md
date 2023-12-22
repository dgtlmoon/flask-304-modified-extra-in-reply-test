Trying to replicate https://github.com/dgtlmoon/changedetection.io/issues/2053

Maybe it's due to some other included module/package?

```bash
$ pip3 install -r requirements.txt
$ ./app.py
```


then (you may need to edit the etag and mod-if dates)

```
curl -vvv 'http://localhost:5000/static' \
    -H 'User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:121.0) Gecko/20100101 Firefox/121.0' \
    -H 'Accept: image/avif,image/webp,*/*' \
    -H 'Accept-Language: de,en-US;q=0.7,en;q=0.3' \
    -H 'Accept-Encoding: gzip, deflate, br' \
    -H 'Connection: keep-alive' \
    -H 'If-Modified-Since: Fri, 22 Dec 2023 10:14:33 GMT' \
    -H 'If-None-Match: "1703239999.0048695-13861-933627416"' \
    -H 'TE: trailers'
```

and now you should be able (or not) to see

```
* Excess found: excess = 5 url = /static (zero-length body)
* Connection #0 to host localhost left intact
```


** BUT **

This does NOT show 'Excess found'

```bash
$ pip3 install -r requirements.txt
$ flask --app app run
```
