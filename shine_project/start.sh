rails new shine \
      --skip-turbolinks \
      --skip-spring \
      --skip-test \
      -d postgresql
yarn install
bundle install
budlle exec rails webpacker:install
foreman start
