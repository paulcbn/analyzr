import { removeToken, setToken } from '../../api';

const initialState = {
  token: localStorage.getItem('token'),
  currentUser: null,
  isAuthenticated: localStorage.getItem('token') !== null,

  loginLoading: false,
  loginErrors: {},

  currentUserLoading: false,
  currentUserErrors: {},
};


export default function auth(state = initialState, action) {
  switch (action.type) {
    case 'CURRENT_USER_LOADING':
      return {
        ...state,
        currentUser: null,
        currentUserLoading: true,
        currentUserErrors: {},
      };
    case 'CURRENT_USER_ERROR':
      removeToken();
      return {
        ...state,
        currentUser: null,
        currentUserLoading: false,
        currentUserErrors: action.data,
        isAuthenticated: false,
      };
    case 'CURRENT_USER_LOADED':
      return {
        ...state,
        currentUser: action.data,
        currentUserLoading: false,
        currentUserErrors: {},
        isAuthenticated: true,
      };

    case 'LOGIN_LOADING':
      removeToken();
      return {
        ...state,
        currentUser: null,
        token: null,
        loginLoading: true,
        loginErrors: {},
        isAuthenticated: false,
      };
    case 'LOGIN_ERROR':
      removeToken();
      return {
        ...state,
        currentUser: null,
        token: null,
        loginLoading: false,
        loginErrors: action.data,
        isAuthenticated: false,
      };
    case 'LOGIN_LOADED':
      setToken(action.data.token);
      return {
        ...state,
        currentUserLoading: true,
        token: action.data.token,
        loginLoading: false,
        loginErrors: {},
        isAuthenticated: true,
      };

    case 'LOGOUT_LOADED':
      removeToken();
      return {
        ...state,
        currentUser: null,
        token: null,
        isAuthenticated: false,
      };

    case 'CLEAR_AUTH_ERRORS':
      return { ...state, loginErrors: {}, registerErrors: {}, currentUserErrors: {} };

    default:
      return state;
  }
}
