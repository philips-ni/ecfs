rails new shine \
      --skip-turbolinks \
      --skip-spring \
      --skip-test \
      -d postgresql
yarn install
bundle install
bundle exec rails webpacker:install
foreman start
