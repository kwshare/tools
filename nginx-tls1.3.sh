mkdir build && cd build

wget  https://nginx.org/download/nginx-1.19.2.tar.gz
tar xf nginx-1.19.2.tar.gz

git clone https://github.com/google/ngx_brotli
cd ngx_brotli && git submodule update --init && cd ..
cd nginx-1.19.2
openssl version|grep 1.1.1

if [ $? -eq 0 ];then
    ./configure --user=www --group=www  --prefix=/usr/local/nginx \
    --add-module=../ngx_brotli  --with-openssl-opt='enable-tls1_3' \
    --with-http_v2_module --with-http_ssl_module --with-http_gzip_static_module \
    --with-http_stub_status_module --with-http_sub_module --with-stream \
    --with-stream_ssl_module \
    --with-compat \
    --with-http_realip_module
  else
    git clone https://github.com/openssl/openssl
      ./configure --user=www --group=www  --prefix=/usr/local/nginx \
    --add-module=../ngx_brotli --with-openssl=../openssl --with-openssl-opt='enable-tls1_3' \
    --with-http_v2_module --with-http_ssl_module --with-http_gzip_static_module \
    --with-http_stub_status_module --with-http_sub_module --with-stream \
    --with-stream_ssl_module \
    --with-compat \
    --with-http_realip_module
fi



