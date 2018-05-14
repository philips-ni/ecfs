class CustomersController < ApplicationController
  PAGE_SIZE = 10
  def index
    respond_to do |format|
      format.html {}
      format.json {
	render json: { customers: @customers  }
      }
    end
  end
end
  
