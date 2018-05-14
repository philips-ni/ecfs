import { Component, Inject } from '@angular/core';
import { Store } from 'redux';
import { AppStore } from './app.store';
import { AppState } from './app.state';

@Component({
  selector: "shine-customer-search",
  template: `
<header>
  <h1 class="h2">Customer Search</h1>
</header>
<section class="search-form">
  <form>
    <label for="keywords" class="sr-only">Keywords</label>
    <input type="text" id="keywords" name="keywords"
	   placeholder="First Name, Last Name, or Email Address"
           [(ngModel)]="keywords.text"
           on-ngModelChange="search($event)"
	   class="form-control input-lg"/>
  </form>
</section>
<section class="search-results" *ngIf="customers">
  <header>
    <h1 class="h3">Results</h1>
  </header>
  <ol class="list-group">
    <li *ngFor="let customer of customers"
	class="list-group-item clearfix">
      <h3 class="pull-right">
	<small class="text-uppercase">Joined</small>
	{{customer.created_at}}
      </h3>
      <h2 class="h3">
	{{customer.first_name}} {{customer.last_name}}
	<small>{{customer.username}}</small>
      </h2>
      <h4>{{customer.email}}</h4>
    </li>
  </ol>
  </section>
`
})
export class AppComponent{
  data: any[];
  keywords: { text: string };
  customers: any[];
  constructor(@Inject(AppStore) private store: Store<AppState>) {
    store.subscribe(() => this.readState());
    this.readState();
    this.keywords =  {text: ""}
  }
  
  readState() {
    const state: AppState = this.store.getState() as AppState;
    this.data = state.data;
    this.customers = this.data
  }
  
  /* 
  ngOnInit(): void{
    this.data = [
      {"first_name": "Fei",
       "last_name": "Ni",
       "username": "fni",
       "email": "feiphilips.ni@veritas.com"
      },
      {"first_name": "Jason",
       "last_name": "Ni",
       "username": "json_ni",
       "email": "jason.ni@veritas.com"
      }
    ];
    this.customers = this.data;
    this.keywords =  {text: ""}
  }
  */
  
  search(): void {
    this.customers = this.data.filter(item => item.first_name.indexOf(this.keywords.text) != -1) 
  }
}

/*
@Component({
  selector: 'hello-angular',
  template: `<h1>Hello {{name}}</h1>`
})
export class AppComponent {
  name = 'Angular!';
}
*/
