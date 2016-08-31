require 'spec_helper'

describe Yell do
  let( :logger ) { Yell.new }

  subject { logger }

  it "should be_kind_of Yell::Logger" do
    expect(subject).to be_a_kind_of(Yell::Logger)
  end

  it "should raise AdapterNotFound when adapter cant be loaded" do
    expect {
      Yell.new :unknownadapter
    }.to raise_error(Yell::AdapterNotFound)
  end

  context ".level" do
    subject { Yell.level }
    it "should be_kind_of Yell::Level" do
      expect(subject).to be_a_kind_of(Yell::Level)
    end
  end

  context ".format" do
    subject { Yell.format( "%m" ) }
    it "should be_kind_of Yell::Formatter" do
      expect(subject).to be_a_kind_of(Yell::Formatter)
    end
  end

  context ".load!" do
    subject { Yell.load!('yell.yml') }

    before do
      mock(Yell::Configuration).load!('yell.yml') { {} }
    end

    it "should be_kind_of Yell::Logger" do
      expect(subject).to be_a_kind_of(Yell::Logger)
    end
  end

  context ".[]" do
    let(:name) { 'test' }

    it "should delegate to the repository" do
      mock(Yell::Repository)[name]

      Yell[name]
    end
  end

  context ".[]=" do
    let(:name) { 'test' }

    it "should delegate to the repository" do
      mock.proxy(Yell::Repository)[name] = logger

      Yell[name] = logger
    end
  end

  context ".env" do
    subject { Yell.env }

    it "should default to YELL_ENV" do
      expect(subject).to eq('test')
    end

    context "fallback to RACK_ENV" do
      before do
        stub(ENV).key?('YELL_ENV') { false }
        mock(ENV).key?('RACK_ENV') { true }

        ENV['RACK_ENV'] = 'rack'
      end

      after { ENV.delete 'RACK_ENV' }

      it "should == 'rack'" do
        expect(subject).to eq('rack')
      end
    end

    context "fallback to RAILS_ENV" do
      before do
        stub(ENV).key?('YELL_ENV') { false }
        stub(ENV).key?('RACK_ENV') { false }
        mock(ENV).key?('RAILS_ENV') { true }

        ENV['RAILS_ENV'] = 'rails'
      end

      after { ENV.delete 'RAILS_ENV' }

      it "should == 'rails'" do
        expect(subject).to eq('rails')
      end
    end

    context "fallback to development" do
      before do
        stub(ENV).key?('YELL_ENV') { false }
        stub(ENV).key?('RACK_ENV') { false }
        stub(ENV).key?('RAILS_ENV') { false }
      end

      it "should == 'development'" do
        expect(subject).to eq('development')
      end
    end
  end

end

