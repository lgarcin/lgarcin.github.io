source "http://rubygems.org"

# Specify your gem's dependencies in yell.gemspec
gemspec

group :development, :test do
  gem "rake"

  gem 'rspec-core', '~> 3'
  gem 'rspec-expectations', '~> 3'
  gem 'rspec-its'
  gem "rr"

  if RUBY_VERSION < "1.9"
    gem 'timecop', '0.6.0'
    gem 'activesupport', '~> 3'
  else
    gem 'timecop'
    gem 'activesupport'

    gem 'pry'
  end

  gem 'simplecov', :require => false, :platform => :ruby_20
  gem 'coveralls', :require => false, :platform => :ruby_20
end

