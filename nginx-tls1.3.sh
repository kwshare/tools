mkdir build && cd build

wget  https://nginx.org/download/nginx-1.19.2.tar.gz
tar xf nginx-1.19.2.tar.gz

git clone https://github.com/google/ngx_brotli
cd ngx_brotli && git submodule update --init && cd ..


git clone https://github.com/openresty/srcache-nginx-module
git clone https://github.com/openresty/redis2-nginx-module
git clone https://github.com/openresty/set-misc-nginx-module
git clone https://github.com/vision5/ngx_devel_kit

wget https://people.freebsd.org/~osa/ngx_http_redis-0.3.9.tar.gz
tar xf ngx_http_redis-0.3.9.tar.gz
 
cd nginx-1.19.2
openssl version|grep 1.1.1

if [ $? -eq 0 ];then
            ./configure --user=www --group=www  --prefix=/usr/local/nginx \
        --add-module=../ngx_brotli --with-openssl-opt='enable-tls1_3' \
        --with-http_v2_module --with-http_ssl_module --with-http_gzip_static_module \
        --with-http_stub_status_module --with-http_sub_module --with-stream \
        --with-stream_ssl_module \
        --with-compat \
        --with-http_realip_module \
        --add-module=../srcache-nginx-module \
        --add-module=../redis2-nginx-module \
        --add-module=../ngx_http_redis-0.3.9 \
        --add-module=../ngx_devel_kit \
        --add-module=../set-misc-nginx-module
  else
            git clone https://github.com/openssl/openssl

            ./configure --user=www --group=www  --prefix=/usr/local/nginx \
        --add-module=../ngx_brotli --with-openssl=../openssl --with-openssl-opt='enable-tls1_3' \
        --with-http_v2_module --with-http_ssl_module --with-http_gzip_static_module \
        --with-http_stub_status_module --with-http_sub_module --with-stream \
        --with-stream_ssl_module \
        --with-compat \
        --with-http_realip_module \
        --add-module=../srcache-nginx-module \
        --add-module=../redis2-nginx-module \
        --add-module=../ngx_http_redis-0.3.9 \
        --add-module=../ngx_devel_kit \
        --add-module=../set-misc-nginx-module
fi

make && make install


