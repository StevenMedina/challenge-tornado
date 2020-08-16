
const app = new Vue({
    el: '#app',
    delimiters: ['[[',']]'],
    data: {
      errors: [],
      tax_id: null,
      business_name: null,
      requested_amount: null,
      owner_social_security_number: null,
      owner_name: null,
      owner_email: null
    },
    methods: {
      checkForm: function (e) {
        if (this.tax_id && this.business_name && this.requested_amount) {
          this.submitLoanApplication();
        }

        this.errors = [];

        if (!this.tax_id) {
          this.errors.push('Tax ID required.');
        }
        if (!this.business_name) {
          this.errors.push('Business Name required.');
        }
        if (!this.requested_amount) {
          this.errors.push('Requested required.');
        }
        if (!this.owner_social_security_number) {
          this.errors.push('Owner Social required.');
        }
        if (!this.owner_name) {
          this.errors.push('Owner Name required.');
        }
        if (!this.owner_email) {
          this.errors.push('Owner Email required.');
        }

      },
      submitLoanApplication: function() {
        axios.post(
            'http://0.0.0.0:8888/loan-application/',
            {
              tax_id: this.tax_id,
              business_name: this.business_name,
              requested_amount: this.requested_amount,
              owner_social_security_number: this.owner_social_security_number,
              owner_name: this.owner_name,
              owner_email: this.owner_email,
            },
            {headers: {
              'Content-type': 'application/x-www-form-urlencoded',
            }
        }).then(response => {
          alert("The loan is " + response.data.message);
        }).catch(function (error) {
          console.log(error);
        });
      }
    }
  })