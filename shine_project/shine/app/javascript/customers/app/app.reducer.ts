/**
 * Counter Reducer
 */
import { Reducer, Action } from 'redux';
import { AppState } from './app.state';
import {
  INCREMENT,
  DECREMENT
} from './app.actions';

const initialState: AppState = {
  data: [
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
  ]
};
			       

// Create our reducer that will handle changes to the state
export const appReducer: Reducer<AppState> =
  (state: AppState = initialState, action: Action): AppState => {
    switch (action.type) {
    case INCREMENT:
	return state;
    case DECREMENT:
	return state
    default:
	return state;
    }
  };
