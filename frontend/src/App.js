import MomentUtils from '@date-io/moment';
import CssBaseline from '@material-ui/core/CssBaseline';
import { ThemeProvider } from '@material-ui/core/styles';
import { MuiPickersUtilsProvider } from '@material-ui/pickers';
import moment from 'moment';
import 'moment/locale/ro';
import React from 'react';
import { Provider } from 'react-redux';
import { applyMiddleware, createStore } from 'redux';
import thunk from 'redux-thunk';
import RootContainer from './components/Routing/RootContainer/RootContainer';
import { rootReducer } from './lib/redux/reducers';
import theme from './lib/theme';

moment.locale('ro');

let store = createStore(rootReducer, applyMiddleware(thunk));

function App() {
  return <>
    <CssBaseline/>
    <MuiPickersUtilsProvider utils={ MomentUtils }>
      <ThemeProvider theme={ theme }>
        <Provider store={ store }>
          <RootContainer/>
        </Provider>
      </ThemeProvider>
    </MuiPickersUtilsProvider>
  </>;
}

export default App;
