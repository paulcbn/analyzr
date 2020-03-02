import { Container } from '@material-ui/core';
import Box from '@material-ui/core/Box';
import Button from '@material-ui/core/Button';
import React from 'react';
import { connect } from 'react-redux';
import { auth } from '../../lib/redux/actions';


const LayoutComponent = ({ children, logout }) => {
  return <Box>
    this view is layouted
    <Button onClick={ logout }>
      Logout
    </Button>
    <Container>
      { children }
    </Container>
  </Box>;
};
const mapStateToProps = () => ({});
const mapDispatchToProps = (dispatch) => ({
  logout: () => dispatch(auth.logout()),
});

const Layout = connect(mapStateToProps, mapDispatchToProps)(LayoutComponent);

export const withLayout = (PageComponent) => {
  return (props) => {
    return <Layout>
      <PageComponent { ...props }/>
    </Layout>;
  };
};
