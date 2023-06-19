# Generate IP Cert

This script generates a self-signed SSL certificate for an IP address.

## Usage

Replace 127.0.0.1 with the desired IP:

```sh
curl -sS https://raw.githubusercontent.com/rezw4n/generate-ip-cert/master/generate-ip-cert.sh |
    bash -s 127.0.0.1
```

This will create two files: `cert.pem` and `key.pem`.

## Motivation

While it's easy to make a self-signed SSL certificate for a hostname, doing it for an IP address
is a bit more complicated. I found several guides on Internet that didn't work for me,
so here's the summary in one script.

Tested on macOS Catalina and Ubuntu.

## References

The process of generating a SAN certificate is described here:

https://geekflare.com/san-ssl-certificate/  
https://support.citrix.com/article/CTX135602  

## License

MIT
