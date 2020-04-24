./configure --user=www --group=www  --prefix=/usr/local/nginx \
--add-module=../ngx_brotli --with-openssl=../openssl --with-openssl-opt='enable-tls1_3' \
--with-http_v2_module --with-http_ssl_module --with-http_gzip_static_module \
--with-http_stub_status_module --with-http_sub_module --with-stream \
--with-stream_ssl_module \
--with-compat \
--with-http_realip_module

