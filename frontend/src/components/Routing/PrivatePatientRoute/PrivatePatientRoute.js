import React, { useMemo } from 'react';
import { Redirect, Route } from 'react-router-dom';
import { deepGet } from '../../../lib/utils';

const PrivatePatientRoute = ({ pageComponent: Page, loadingComponent: Loading, notAllowedComponent: NotAllowed, errorRedirectRoute, authState, ...otherProps }) => {
  const { isPatient, loading, isAuthenticated } = useMemo(() => ({
    loading: deepGet(authState, 'loginLoading', false),
    isAuthenticated: deepGet(authState, 'isAuthenticated', false),
    isPatient: deepGet(authState, 'currentUser.userType', 'doctor') === 'patient',
  }), [ authState ]);
  console.log({ isPatient});
  return <Route
    { ...otherProps }

    render={ props => {
      if (loading)
        return <Loading { ...props }/>;
      if (!isAuthenticated)
        return <Redirect to={ errorRedirectRoute }/>;
      if (!isPatient)
        return <NotAllowed/>;

      return <Page { ...props } />;
    } }
  />;
};

export default PrivatePatientRoute;
