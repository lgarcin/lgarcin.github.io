# -*- encoding: utf-8 -*-
# stub: wdm 0.1.1 ruby lib
# stub: ext/wdm/extconf.rb

Gem::Specification.new do |s|
  s.name = "wdm"
  s.version = "0.1.1"

  s.required_rubygems_version = Gem::Requirement.new(">= 0") if s.respond_to? :required_rubygems_version=
  s.require_paths = ["lib"]
  s.authors = ["Maher Sallam"]
  s.date = "2015-07-09"
  s.description = "Windows Directory Monitor (WDM) is a library which can be used to monitor directories for changes. It's mostly implemented in C and uses the Win32 API for a better performance."
  s.email = ["maher@sallam.me"]
  s.extensions = ["ext/wdm/extconf.rb"]
  s.files = ["ext/wdm/extconf.rb"]
  s.homepage = "https://github.com/Maher4Ever/wdm"
  s.required_ruby_version = Gem::Requirement.new(">= 1.9.2")
  s.rubygems_version = "2.5.1"
  s.summary = "Windows Directory Monitor (WDM) is a threaded directories monitor for Windows."

  s.installed_by_version = "2.5.1" if s.respond_to? :installed_by_version

  if s.respond_to? :specification_version then
    s.specification_version = 4

    if Gem::Version.new(Gem::VERSION) >= Gem::Version.new('1.2.0') then
      s.add_development_dependency(%q<rake-compiler>, [">= 0"])
      s.add_development_dependency(%q<rspec>, [">= 0"])
      s.add_development_dependency(%q<guard-rspec>, [">= 0"])
      s.add_development_dependency(%q<guard-shell>, [">= 0"])
      s.add_development_dependency(%q<pry>, [">= 0"])
    else
      s.add_dependency(%q<rake-compiler>, [">= 0"])
      s.add_dependency(%q<rspec>, [">= 0"])
      s.add_dependency(%q<guard-rspec>, [">= 0"])
      s.add_dependency(%q<guard-shell>, [">= 0"])
      s.add_dependency(%q<pry>, [">= 0"])
    end
  else
    s.add_dependency(%q<rake-compiler>, [">= 0"])
    s.add_dependency(%q<rspec>, [">= 0"])
    s.add_dependency(%q<guard-rspec>, [">= 0"])
    s.add_dependency(%q<guard-shell>, [">= 0"])
    s.add_dependency(%q<pry>, [">= 0"])
  end
end
