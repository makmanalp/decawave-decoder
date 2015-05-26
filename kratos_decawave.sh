# Port setting
stty -F /dev/kratos_decawave raw speed 115200

echo '?' > /dev/kratos_decawave
echo '?' > /dev/kratos_decawave

echo '#' > /dev/kratos_decawave
echo '#' > /dev/kratos_decawave
echo '#' > /dev/kratos_decawave
echo '#' > /dev/kratos_decawave

sleep 2
stdbuf -oL -eL ./spisniffer -d /dev/kratos_decawave | python -u lcd_spi_decode.py
