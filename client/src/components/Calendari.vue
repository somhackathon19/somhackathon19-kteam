<template>
  <div class="container">
    <full-calendar :config="config" :events="events"/>
  </div>
</template>

<script>
import { FullCalendar } from 'vue-full-calendar'
import store from '../store'
import 'fullcalendar/dist/locale/ca'
import moment from 'moment';
export default {
  name: "Calendari",
  components: {
    FullCalendar
  },
  data() {
    return {
			events: [
				{
					title: 'test',
					start: moment(),
          end: moment().add(1, 'd'),
          editable: false
				},
				{
					title: 'another test',
					start: moment().add(2,'d'),
					end: moment().add(2, 'd').add(2, 'h'),
          editable: false
				},
			],
			config: {
        defaultView: 'month',
        locale: 'ca',
      },
      created() {
        for (let i = 0; i < store.state.events.length; ++i) {
          let event = store.state.events[i];
          
        }
      }
    };
  }
};
</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->
<style scoped>
</style>
