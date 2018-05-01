class CustomersController < ApplicationController
  PAGE_SIZE = 10
  def index
    @page = (params[:page] || 0).to_i
    if params[:keywords].present?
      @keywords = params[:keywords]
      customer_search_term = CustomerSearchTerm.new(@keywords)
      @all_customers = Customer.where(customer_search_term.where_clause,
				  customer_search_term.where_args).
	order(customer_search_term.order)
      @customers = @all_customers.offset(PAGE_SIZE * @page).limit(PAGE_SIZE)
      @page_amount = @all_customers.length / PAGE_SIZE + 1
    else
      @customers = []
      @page_amount = 0
      # @customers = Customer.all.limit(20)
    end
  end
end
  
