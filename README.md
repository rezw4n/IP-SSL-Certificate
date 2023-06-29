# Generate IP Cert

This script generates a self-signed SSL certificate for an IP address.

## Usage

Open powershell as administrator. Changed directory to the downloaded repository. Run the script using ```python SSL.py```

This will create two files: `cert.pem` and `cert-key.pem`.

## Motivation

While it's easy to make a self-signed SSL certificate for a hostname, doing it for an IP address
is a bit more complicated. I found several guides on Internet that didn't work for me,
so I created one that actually works.

Tested on Windows OS.

## License

MIT
